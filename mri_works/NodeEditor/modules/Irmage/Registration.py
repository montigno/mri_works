class Non_linear_registration_for_Atlases:
    def __init__(self,
                 image_fixed='path',
                 atlas_template_moved='path',
                 atlas_label_moved='path',
                 output_template_name='path',
                 output_label_name='path',
                 interpolator="enumerate(('linear',\
                                          'nearestNeighbor',\
                                          'multiLabel',\
                                          'genericlabel',\
                                          'gaussian',\
                                          'bSpline',\
                                          'cosineWindowedSinc',\
                                          'welchWindowedSinc',\
                                          'hammingWindowedSinc',\
                                          'lanczosWindowedSinc'))",
                 transform="enumerate(('Translation',\
                                       'Rigid',\
                                       'Similarity',\
                                       'QuickRigid',\
                                       'DenseRigid',\
                                       'BOLDRigid',\
                                       'Affine',\
                                       'AffineFast',\
                                       'BOLDAffine',\
                                       'TRSAA',\
                                       'ElasticSyN',\
                                       'SyN',\
                                       'SyNRA',\
                                       'SyNOnly',\
                                       'SyNCC',\
                                       'SyNabp',\
                                       'SyNBold',\
                                       'SyNBoldAff',\
                                       'SyNAggro',\
                                       'TVMSQ',\
                                       'TVMSQC'))"):
        import ants
        img_fi =  ants.image_read(image_fixed)
        atlas_temp_mo = ants.image_read(atlas_template_moved)
        atlas_lab_mo = ants.image_read(atlas_label_moved)
        warpedmoveout = ants.registration(fixed=img_fi,
                                      moving=atlas_temp_mo,
                                      type_of_transform = transform)
        imagetransformed = ants.apply_transforms(fixed=warpedmoveout['warpedmovout'], moving=atlas_lab_mo,
                                           transformlist = warpedmoveout['fwdtransforms'],
                                           interpolator=interpolator)
        ants.image_write(warpedmoveout['warpedmovout'], output_template_name)
        ants.image_write(imagetransformed, output_label_name)
        self.temp_reg = output_template_name
        self.lab_reg = output_label_name
        
    def out_template_registred(self:'path'):
        return self.temp_reg
    
    def out_label_registred(self:'path'):
        return self.lab_reg
    
###############################################################################

class Non_linear_registration_multiple_Images:
    def __init__(self,
                 image_fixed='path',
                 image_moved='path',
                 images_apply_transform=['path'],
                 output_moved_name='path',
                 suffix_transformed_name='_transformed',
                 interpolator="enumerate(('linear',\
                                          'nearestNeighbor',\
                                          'multiLabel',\
                                          'genericlabel',\
                                          'gaussian',\
                                          'bSpline',\
                                          'cosineWindowedSinc',\
                                          'welchWindowedSinc',\
                                          'hammingWindowedSinc',\
                                          'lanczosWindowedSinc'))",
                 transform="enumerate(('Translation',\
                                       'Rigid',\
                                       'Similarity',\
                                       'QuickRigid',\
                                       'DenseRigid',\
                                       'BOLDRigid',\
                                       'Affine',\
                                       'AffineFast',\
                                       'BOLDAffine',\
                                       'TRSAA',\
                                       'ElasticSyN',\
                                       'SyN',\
                                       'SyNRA',\
                                       'SyNOnly',\
                                       'SyNCC',\
                                       'SyNabp',\
                                       'SyNBold',\
                                       'SyNBoldAff',\
                                       'SyNAggro',\
                                       'TVMSQ',\
                                       'TVMSQC'))"):
        import ants
        import os
        img_fi =  ants.image_read(image_fixed)
        img_mo = ants.image_read(image_moved)
        warpedmoveout = ants.registration(fixed=img_fi,
                                      moving=img_mo,
                                      type_of_transform = transform)
        list_transf = []
        for lst_img in images_apply_transform:
            dir = os.path.dirname(lst_img)
            tmp = os.path.basename(lst_img)
            name = ('.').join(tmp.split('.')[:-1])
            ext = tmp.split('.')[-1]
            out_img_transform = os.path.join(dir, name + suffix_transformed_name + '.'+ext)
            img_tra = ants.image_read(lst_img)
            imagetransformed = ants.apply_transforms(fixed=warpedmoveout['warpedmovout'], moving=img_tra,
                                           transformlist = warpedmoveout['fwdtransforms'],
                                           interpolator=interpolator)
            ants.image_write(imagetransformed, out_img_transform)
            list_transf.append(out_img_transform)
        ants.image_write(warpedmoveout['warpedmovout'], output_moved_name)
        self.img_reg = output_moved_name
        self.img_tra = list_transf
        
    def out_image_registred(self:'path'):
        return self.img_reg
    
    def out_image_transformed(self:'list_path'):
        return self.img_tra
