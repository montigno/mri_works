class Nifti_header():

    def __init__(self, nii_image='path'):
        import nibabel as nib
        img = nib.load(nii_image)
        self.hdr = img.header

    def nii_hdr(self: 'str'):
        return self.hdr

##############################################################################


class Nifti_affine_quaternion():

    def __init__(self, nii_image='path'):
        import nibabel as nib
        img = nib.load(nii_image)
        hdr = img.header
        self.affine = hdr.get_sform(coded=True)
        self.quaternions = hdr.get_qform_quaternion()

    def nii_affine(self: 'str'):
        return self.affine

    def nii_quaternions(self: 'str'):
        return self.quaternions

##############################################################################


class Nifti_getInfo():

    def __init__(self,
                 nii_image='path',
                 get_info="enumerate(('get_info',\
                                      'get_dim_info',\
                                      'get_sform',\
                                      'get_base_affine',\
                                      'get_qform',\
                                      'get_qform_quaternion',\
                                      'get_slope_inter',\
                                      'get_xyzt_units'))"):
        import nibabel as nib
        img = nib.load(nii_image)
        hdr = img.header
        info_val = getattr(hdr, get_info, None)
        try:
            self.info_val = info_val()
        except Exception as e:
            self.info_val = type(info_val)

    def nii_info(self: 'str'):
        return self.info_val

##############################################################################


class Nifti_rawInfo():

    def __init__(self,
                 nii_image='path',
                 structarr="enumerate(('sizeof_hdr',\
                                       'data_type',\
                                       'db_name',\
                                       'extents',\
                                       'session_error',\
                                       'regular',\
                                       'dim_info',\
                                       'dim',\
                                       'intent_p1',\
                                       'intent_p2',\
                                       'intent_p3',\
                                       'intent_code',\
                                       'datatype',\
                                       'bitpix',\
                                       'slice_start',\
                                       'pixdim',\
                                       'vox_offset',\
                                       'scl_slope',\
                                       'scl_inter',\
                                       'slice_end',\
                                       'slice_code',\
                                       'xyzt_units',\
                                       'cal_max',\
                                       'cal_min',\
                                       'slice_duration',\
                                       'toffset',\
                                       'glmax',\
                                       'glmin',\
                                       'descrip',\
                                       'aux_file',\
                                       'qform_code',\
                                       'sform_code',\
                                       'quatern_b',\
                                       'quatern_c',\
                                       'quatern_d',\
                                       'qoffset_x',\
                                       'qoffset_y',\
                                       'qoffset_z',\
                                       'srow_x',\
                                       'srow_y',\
                                       'srow_z',\
                                       'intent_name',\
                                       'magic'))"):
        import nibabel as nib
        img = nib.load(nii_image)
        hdr = img.header

        self.str = hdr.structarr[structarr].tolist()

    def out_structarr(self: 'list_str'):
        return self.str
