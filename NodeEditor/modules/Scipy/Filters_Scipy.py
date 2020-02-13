class Sobel():
    def __init__(self,image=[[0.0]]):
        from scipy import ndimage
        self.ax = ndimage.sobel(image)
    
    def Sobel(self:'array_float'):
        return self.ax
    
################################################

class Prewitt():
    def __init__(self,image=[[0.0]]):
        from scipy import ndimage
        self.ax = ndimage.prewitt(image)
    
    def Prewitt(self:'array_float'):
        return self.ax
    
################################################

class Median():
    def __init__(self,image=[[0.0]],size=1):
        from scipy import ndimage
        self.ax = ndimage.median_filter(image, size)
    
    def Median(self:'array_float'):
        return self.ax
    
################################################

class Laplace():
    def __init__(self,image=[[0.0]]):
        from scipy import ndimage
        self.ax = ndimage.laplace(image)
    
    def Laplace(self:'array_float'):
        return self.ax
    
################################################

class Gaussian_filter():
    def __init__(self,image=[[0.0]], sigma=1):
        from scipy import ndimage
        self.ax = ndimage.gaussian_filter(image,sigma=sigma)
        
    def Gaussian(self:'array_float'):
        return self.ax
        
################################################

class Gaussian_laplace():
    def __init__(self,image=[[0.0]], sigma=1):
        from scipy import ndimage
        self.ax = ndimage.gaussian_laplace(image,sigma=sigma)
        
    def Gaussian(self:'array_float'):
        return self.ax
        
        
        
        