class Open_TIFF:
    def __init__(self, file_tiff='path'):
        from PIL import Image, ImageOps
        import numpy as np
        img = Image.open(file_tiff)
        nb = img.n_frames
        self.imarray = []
        for i in range(nb):
            img.seek(i)
            self.imarray.append(np.array(img))
        self.imarray = np.array(self.imarray)
        self.imarray = self.imarray.transpose(2,1,0)
        
    def out_tiff(self:'array_float'):
        return self.imarray