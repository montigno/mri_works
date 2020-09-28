class MatPlotLib:
    def __init__(self,
                 sourceFile='path',
                 title='original',
                 display_mode="enumerate(('ortho', 'x', 'y', 'z', 'yx', 'xz', 'yz'))",
                 dim=1, draw_cross=False, annotate=False):
        from nilearn import plotting
        plotting.plot_anat(sourceFile,
                           title=title,
                           display_mode=display_mode,
                           dim=dim,
                           draw_cross=draw_cross,
                           annotate=annotate)
        plotting.show()

###############################################################################


class MatPlotCurve:
    def __init__(self, data=[[0.0]], x=[0.0]):
        try:
            import matplotlib.pyplot as plt
            for lst in data:
                plt.plot(x, lst)
            plt.show()
        except ImportError:
            pass

###############################################################################


class MatPlotCurve2:
    def __init__(self, data=[0.0], x=[0.0]):
        try:
            import matplotlib.pyplot as plt
            plt.plot(x, data)
            plt.show()
        except ImportError:
            pass

###############################################################################


class Display_Nifti_Niwidget:
    def __init__(self, path_image='path'):
        from niwidgets import NiftiWidget
        import nilearn.plotting as nip
        my_widget = NiftiWidget(path_image)
        my_widget.nifti_plotter(plotting_func=nip.plot_glass_brain)

###############################################################################
