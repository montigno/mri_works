class Matplotlib_image():
    def __init__(self, image=[[0.0]], title=''):
        from scipy import ndimage
        import matplotlib.pyplot as plt
        if len(image.shape) == 3:
            image = image[:, :, int(image.shape[2]/2)]
        if len(image.shape) == 4:
            image = image[:, :, int(image.shape[2]/2), int(image.shape[3]/2)]
        if len(image.shape) == 5:
            image = image[:, :, int(image.shape[2]/2), int(image.shape[3]/2), int(image.shape[4]/2)]

        image = ndimage.rotate(image, -90)
        plt.ion()
        fig, ax = plt.subplots()
#         delta_f = 5.0
#         axcolor = 'lightgoldenrodyellow'
#         sl1 = plt.axes([0.25, 0, 0.65, 0.03], facecolor=axcolor)
#         sl2 = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
#         sfreq = Slider(sl1, 'sl1', 0.1, 30.0, valinit=1)
#         samp = Slider(sl2, 'sl2', 0.1, 10.0, valinit=2)

        ax.imshow(image, cmap=plt.cm.gray)
        ax.set_title(title)
        plt.show()

###############################################################################
