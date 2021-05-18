class sk_threshold_multiotsu:
    def __init__(self, image=[[0.0]], **options):
        from skimage.filters import threshold_multiotsu
        self.thresholds = threshold_multiotsu(image)

    def multi_otsu(self:'list_float'):
        return self.thresholds