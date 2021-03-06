class ants_registration():
    def __init__(self,
                 ants_image_fixed=[[0.0]],
                 ants_image_moving=[[0.0]],
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
                                       'TVMSQC'))", **options):
        import ants
        self.mytx = ants.registration(fixed=ants_image_fixed,
                                      moving=ants_image_moving,
                                      type_of_transform = transform,
                                      **options)
        print('type = ', self.mytx.items())

    def warpedmovout(self:'array_float'):
        return self.mytx['warpedmovout']

    def warpedfixout(self:'array_float'):
        return self.mytx['warpedfixout']

    def fwdtransforms(self:'list_str'):
        return self.mytx['fwdtransforms']

    def invtransforms(self:'list_str'):
        return self.mytx['invtransforms']

##############################################################################

class ants_apply_transform():
    def __init__(self,
                 ants_image_fixed=[[0.0]],
                 ants_image_moving=[[0.0]],
                 transformlist=[''],
                 **options):
        import ants
        self.trans_img = ants.apply_transforms( fixed=ants_image_fixed, moving=ants_image_moving,
                                           transformlist = transformlist, **options)

    def img_transformed(self:'array_float'):
        return self.trans_img

##############################################################################

class ants_affine_initializer():
    def __init__(self, ants_image_fixed=[[0.0]], ants_image_moving=[[0.0]], **options):
        import ants
        self.txfile = ants.affine_initializer(ants_image_fixed, ants_image_moving, **options)
        
    def file_transf(self:'path'):
        return self.txfile
    
##############################################################################

class ants_reorient_image():
    def __init__(self,
                 ants_image=[[0.0]],
                 axis1=(1,0),
                 **options):
        import ants
        ants.reorient_image(ants_image, axis1, **options)
        self.img_oriented = ants_image
        
    def ants_image_reoriented(self:'array_float'):
        return self.img_oriented
        
        