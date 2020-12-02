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
        self.temp_reg = ants.image_write(warpedmoveout['warpedmovout'], output_template_name)
        self.lab_reg = ants.image_write(imagetransformed, output_label_name)
        
    def out_template_registred(self:'path'):
        return self.temp_reg
    
    def out_label_registred(self:'path'):
        return self.lab_reg
