class resize():
    def __init__(self, image=[[0.0]], output_shape=(128,128,64), **options):
        from skimage import transform
        self.a = transform.resize(image, output_shape, **options)

    def image_resize(self:'array_float'):
        return self.a        