class ants_kmeans_segmentation():
    def __init__(self, ants_image=[[0.0]], k=3, **options):
        import ants
        self.seg = ants.kmeans_segmentation(ants_image, k, **options)
        print(self.seg)
        
    def ants_kseg(self:'array_float'):
        return self.seg['segmentation']
    
    def ants_probabilities(self:'array_float'):
        return self.seg['probabilityimages']
    
##############################################################################

class ants_kelly_kapowski():
    def __init__(self,
                 s_ants_image=[[0.0]],
                 g_ants_image=[[0.0]],
                 w_ants_image=[[0.0]],
                 its=45,
                 r=0.5,
                 m=1):
        import ants
        self.ants_kk = ants.kelly_kapowski(s=s_ants_image,
                                           g=g_ants_image,
                                           w=w_ants_image,
                                           its=its,
                                           r=r,
                                           m=m)
        
    def ants_kk(self:'array_float'):
        return self.ants_kk

##############################################################################

class ants_atropos():
    def __init__(self,
                 ants_image=[[0.0]],
                 mask_ants=[[0.0]],
                 **options):
        import ants
        self.atropos = ants.atropos(a = ants_image,
                                    x = mask_ants,
                                    **options)
        
    def ants_atropos_seg(self:'array_float'):
        return self.atropos['segmentation']
    
    def ants_atropos_probabilities(self:'array_float'):
        return self.atropos['probabilityimages']

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
        
        
        
        
        