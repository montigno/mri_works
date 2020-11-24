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
                                       'TVMSQC'))" ):
        import ants
#         fi = ants.image_read(fixed)
#         mi = ants.image_read(moving)
        self.mytx = ants.registration(fixed=ants_image_fixed, moving=ants_image_moving, type_of_transform = transform )
        print('type = ', self.mytx.items())
#         mywarpedimage = ants.apply_transforms( fixed=fi, moving=mi,
#                                            transformlist=mytx['fwdtransforms'] )
#         img = mywarpedimage.to_nibabel()
#         self.img = img.get_fdata()
        
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
    def __init__(self, ants_image_fixed=[[0.0]], ants_image_moving=[[0.0]], transformlist=['']):
        import ants
        self.trans_img = ants.apply_transforms( fixed=ants_image_fixed, moving=ants_image_moving,
                                           transformlist = transformlist)
        
    def img_transformed(self:'array_float'):
        return self.trans_img
                                           
                                           
                                           
                                           