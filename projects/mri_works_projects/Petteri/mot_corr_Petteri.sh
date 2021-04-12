#export PATH=$PATH:/usr/lib/ants/

cd /home/petteri/Data/Motion_correction

subjs=`ls -d Subj*`

echo $subjs

# for each directory in data directory
for ddd in $subjs; do
  cd $ddd/ZTE
  sw_file=ZTE_new.nii
  ref_file=ZTE_3d_bm_N4.nii.gz

  # echo $sw_file
  if [ -f rrr_${sw_file}.gz ]
  then
      echo coregistered file found - $ddd
      cd ../..
      continue
  fi

  if [ -d splits ]
  then
      echo test
  else
      mkdir splits
  fi
  cd splits
  pwd

  if [ -f $ref_file ]
  then
      echo file $ref_file exists
  else
      # construct a reference volume
      bet2 ../mean.nii.gz mean_bm -m -f 0.75
      echo N4BiasFieldCorrection --image-dimensionality 3 --input-image mean_bm.nii.gz --convergence [1000x1000x1000,1.e-5] --output $ref_file --bspline-fitting [1x1x1,4] --mask-image mean_bm_mask.nii.gz
      N4BiasFieldCorrection --image-dimensionality 3 --input-image mean_bm.nii.gz --convergence [1000x1000x1000,1.e-5] --output $ref_file --bspline-fitting [1x1x1,4] --mask-image mean_bm_mask.nii.gz
  fi

  
  bc_swift_file=ZTE_N4.nii.gz

  if [ -f $bc_swift_file ]
  then
      echo file $bc_swift_file exists
  else
      echo N4BiasFieldCorrection --image-dimensionality 4 --input-image ../visual_cut.nii --convergence [1000x1000x1000,1.e-4] --output $bc_swift_file --bspline-fitting [1x1x1x1,2]
      N4BiasFieldCorrection --image-dimensionality 4 --input-image ../visual_cut.nii --convergence [1000x1000x1000,1.e-4] --output $bc_swift_file --bspline-fitting [1x1x1x1,2]
  fi
  
  # split the 4D set to 3D sets
  if [ -f bc_split_0000.nii.gz ]
  then
      echo split files found
  else
      fslsplit $bc_swift_file bc_split_ -t
  fi
  
  spfiles=`ls bc_split_*[0-9].nii.gz`
#  echo $spfiles
#  exit 0

  prev_mat=Identity
  
  for ff in $spfiles; do
      gg=`echo $ff | sed s/\.nii\.gz//`
      echo $gg
      if [ -f a_${gg}_wrpd.nii.gz ]
      then
	  echo warped files found
      else
#	  echo	  antsRegistration --dimensionality 3 --output [x_${gg}_,a_${gg}_wrpd.nii.gz] --interpolation Linear --winsorize-image-intensities [0.005,0.995] --transform Rigid[0.1] --metric MI[$ref_file,$ff,1,16,Regular,0.2] --convergence [800x600,1e-7] --shrink-factors 2x1 --smoothing-sigmas 2x0vox --masks mean_bm_mask.nii.gz --verbose
	echo  antsRegistration --dimensionality 3 --output [x_${gg}_,a_${gg}_wrpd.nii.gz] --interpolation Linear --winsorize-image-intensities [0.005,0.995] --initial-moving-transform $prev_mat --transform Rigid[0.1] --metric MI[$ref_file,$ff,1,8,Regular,0.1] --convergence [800x600,1e-7] --shrink-factors 2x1 --smoothing-sigmas 2x0vox --masks mean_bm_mask.nii.gz --verbose --use-histogram-matching 0
	#	antsRegistration --dimensionality 3 --output [x_${gg}_,a_${gg}_wrpd.nii.gz] --interpolation Linear --winsorize-image-intensities [0.0005,0.9995] --use-histogram-matching 0 --initial-moving-transform $prev_mat --transform Rigid[0.05] --metric MI[$ref_file,$ff,1,6,Regular,0.8] --convergence [800x800,1e-7] --shrink-factors 2x1 --smoothing-sigmas 0x0vox --masks mean_bm_mask.nii.gz --verbose
	antsRegistration --dimensionality 3 --output [x_${gg}_,a_${gg}_wrpd.nii.gz] --interpolation Linear --initial-moving-transform $prev_mat --winsorize-image-intensities [0.0005,0.9995] --use-histogram-matching 0 --transform Rigid[0.05] --metric GC[$ref_file,$ff,1,4,Regular,0.5] --convergence [800x800,1e-7] --shrink-factors 2x1 --smoothing-sigmas 2x0vox --masks mean_bm_mask.nii.gz --verbose
      fi
      prev_mat=x_${gg}_0GenericAffine.mat
      echo $prev_mat
      #sleep 20
  done
#  exit 0
  fslmerge -t visual_cut_${sw_file} a_bc_split_*.nii.gz
#exit 0
  # cleaning
#  rm a_S0_split_*
#  rm S0_split_*
#  rm ref_start.nii.gz

  ### apply S0 motion correction to XX dataset
  # split 4D set to 3D volumes
  # apply  co-registration to the 3D volumes
      # merge 3D volumes back to a 4D set
  if [ -f orig_split_0300.nii.gz ]
  then
      echo warped files found
  else
      fslsplit ../$sw_file orig_split_ -t %%%%%%%%%%%%%%%%%%% not working
  fi
  
  for ff in $spfiles; do
      gg=`echo $ff | sed s/bc/orig/`
      echo $gg
      trns=`echo $ff | sed s/^bc/x_bc/ | sed s/\.nii\.gz/_0GenericAffine\.mat/`
      echo $trns

      echo antsApplyTransforms --dimensionality 3 --float 0 --input $gg --reference-image $ref_file --output a_${gg} --interpolation Linear --transform $trns
      antsApplyTransforms --dimensionality 3 --float 0 --input $gg --reference-image $ref_file --output a_${gg} --interpolation Linear --transform $trns
  done

  # collect co-registered 3D volumes to a 4D set
  fslmerge -t ../rrr_${sw_file} a_orig_split_*.nii.gz

  # cleaning
#  rm a_R2_split*
#  rm R2_split_*
#  rm x_S0_split*
  cd ../../..
#  pwd
#  exit 0
done

cd ..

#
#
