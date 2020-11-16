class ants_registration():
    def __init__(self,
                 fixed='path',
                 moving='path',
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
                                       'TVMSQC'))",
                 file_out='path'):
        import ants
        fi = ants.image_read(fixed)
        mi = ants.image_read(moving)
        mytx = ants.registration(fixed=fi, moving=mi, type_of_transform = transform )
        print('type = ', mytx.items())
        mywarpedimage = ants.apply_transforms( fixed=fi, moving=mi,
                                           transformlist=mytx['invtransforms'] )
        img = mywarpedimage.to_nibabel()
        self.img = img.get_fdata()
        
    def img_reg(self:'array_float'):
        return self.img
