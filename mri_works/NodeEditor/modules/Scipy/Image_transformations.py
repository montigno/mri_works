class rotate:
    def __init__(self, image=[[0.0]], angle=0):
        from scipy import ndimage
        self.rot_img = ndimage.rotate(image, angle)

    def rotate_img(self: 'array_float'):
        return self.rot_img
