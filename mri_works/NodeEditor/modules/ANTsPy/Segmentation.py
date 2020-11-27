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
        
        
        
        