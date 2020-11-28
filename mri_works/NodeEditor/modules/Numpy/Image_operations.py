from grpc.framework.foundation.logging_pool import pool
class addImage_dyn():
    def __init__(self, image1=[[0.0]], image2=[[0.0]], **dynamicsInputs):
        import numpy as np
        image1 = np.array(image1)
        image2 = np.array(image2)
        self.image = np.add(image1, image2)
        for di in dynamicsInputs:
            self.image = np.add(self.image, np.array(dynamicsInputs[di]))

    def image(self: 'array_float'):
        return self.image

###############################################################


class subtractImage_dyn:
    def __init__(self, image1=[[0.0]], image2=[[0.0]], **dynamicsInputs):
        import numpy as np
        image1 = np.array(image1)
        image2 = np.array(image2)
        self.image = np.subtract(image1, image2)
        for di in dynamicsInputs:
            self.image = np.subtract(self.image, np.array(dynamicsInputs[di]))

    def image(self: 'array_float'):
        return self.image

###############################################################


class MultiplyImage_dyn:
    def __init__(self, image1=[[0.0]], image2=[[0.0]], **dynamicsInputs):
        import numpy as np
        image1 = np.array(image1)
        image2 = np.array(image2)
        self.image = np.multiply(image1, image2)
        for di in dynamicsInputs:
            self.image = np.multiply(self.image, np.array(dynamicsInputs[di]))

    def image(self: 'array_float'):
        return self.image

###############################################################


class DivideImage_dyn:
    def __init__(self, image1=[[0.0]], image2=[[0.0]], **dynamicsInputs):
        import numpy as np
        image1 = np.array(image1)
        image2 = np.array(image2)
        try:
            self.image = np.divide(image1, image2)
            for di in dynamicsInputs:
                self.image = np.divide(self.image, np.array(dynamicsInputs[di]))
        except Exception as e:
            self.image = image1

    def image(self: 'array_float'):
        return self.image

###############################################################

class AbsImage:
    def __init__(self, image=[[0.0]]):
        import numpy as np
        self.imageAbs = np.absolute(image)

    def abs_image(self: 'array_float'):
        return self.imageAbs
    
###############################################################

class Invert_image:
    def __init__(self, image=[[0.0]]):
        import numpy as np
        self.imageInv = -np.array(image)

    def inv_image(self: 'array_float'):
        return self.imageInv
    
###############################################################

class MaxPool3D:
    def __init__(self, image=[[0.0]], size_filter=1, stride=1):
        import numpy as np
        img = np.array(image)
        print('img shape = ', img.shape)
        image_height, image_width, image_depth = img.shape
        output_height = (image_height - size_filter) // stride + 1
        output_width = (image_width - size_filter) // stride + 1
        pool = np.zeros((output_height, output_width, image_depth))
        for i in range(output_height):
            for j in range(output_width):
                pool[i, j, :] = np.max(img[i*stride:i*stride+size_filter, j*stride:j*stride+size_filter, :])
        self.img_pool = pool
        
    def image_pool(self:'array_float'):
        return self.img_pool



