class concat_images:
    def __init__(self, filenames=['path']):
        import nibabel.funcs as nb
        img_conc = nb.concat_images(filenames, check_affines=False, axis=None)
        self.img = img_conc.get_fdata()
        self.header = img_conc.header

    def concat_img(self:'array_float'):
        return self.img
    
    def header_img(self:'str'):
        return self.header