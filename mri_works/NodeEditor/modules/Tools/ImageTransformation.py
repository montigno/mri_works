class reslice():
    def __init__(self, image=[[0.0]], order=[0]):
        import numpy as np
        self.image = np.transpose(image, order)

    def image(self: 'array_float'):
        return self.image
