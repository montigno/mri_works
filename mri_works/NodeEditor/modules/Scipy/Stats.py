class scipy_threshold:
    def __init__(self,image=[[0.0]], threshmin=0.0, threshmax=10.0, newval=0.0):
        import numpy as np
        from scipy import stats
        self.img_thrs = stats.threshold(np.array(image),
                                        threshmin=threshmin,
                                        threshmax=threshmax,
                                        newval=newval)
        
    def image_thrs(self:'array_float'):
        return self.img_thrs