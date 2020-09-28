class addImage():
    def __init__(self, image1=[[0.0]], image2=[[0.0]]):
        import numpy as np
        image1 = np.array(image1)
        image2 = np.array(image2)
        self.image = np.add(image1, image2)

    def image(self: 'array_float'):
        return self.image

###############################################################


class subtractImage:
    def __init__(self, image1=[[0.0]], image2=[[0.0]]):
        import numpy as np
        image1 = np.array(image1)
        image2 = np.array(image2)
        self.image = np.subtract(image1, image2)
        self.imageAbs = np.absolute(self.image)

    def image(self: 'array_float'):
        return self.image

    def imageAbs(self: 'array_float'):
        return self.imageAbs

###############################################################


class MultiplyImage:
    def __init__(self, image1=[[0.0]], image2=[[0.0]]):
        import numpy as np
        image1 = np.array(image1)
        image2 = np.array(image2)
        self.image = np.multiply(image1, image2)
        self.imageAbs = np.absolute(self.image)

    def image(self: 'array_float'):
        return self.image

    def imageAbs(self: 'array_float'):
        return self.imageAbs

###############################################################


class DivideImage:
    def __init__(self, image1=[[0.0]], image2=[[0.0]]):
        import numpy as np
        image1 = np.array(image1)
        image2 = np.array(image2)
        try:
            self.image = np.divide(image1, image2)
        except Exception as e:
            self.image = image1
        self.imageAbs = np.absolute(self.image)

    def image(self: 'array_float'):
        return self.image

    def imageAbs(self: 'array_float'):
        return self.imageAbs

###############################################################
