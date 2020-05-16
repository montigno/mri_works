class Choose_file:
    def __init__(self, fileDefault='path',
                 extension='*', title='Select a file'):
        import os.path
        from PyQt5.QtWidgets import QFileDialog
        self.fileChosen = fileDefault
        if fileDefault is 'path' or not os.path.exists(fileDefault):
            fileCh = QFileDialog.getOpenFileName(
                            None,
                            title,
                            '',
                            extension,
                            None,
                            QFileDialog.DontUseNativeDialog)
            if fileCh[0]:
                self.fileChosen = fileCh[0]

    def filePath(self: 'path'):
        return self.fileChosen


class image_Rescale():
    def __init__(self, in_file='path', ref_file='path', **options):
        from nipype.interfaces.image import Rescale
        invert_t1w = Rescale(invert=True)
        invert_t1w.inputs.in_file = in_file
        invert_t1w.inputs.ref_file = ref_file
        for ef in options:
            setattr(invert_t1w.inputs, ef, options[ef])
        self.res = invert_t1w.run()

    def out_file(self: 'path'):
        return self.res.outputs.out_file


class MatPlotLib:
    def __init__(self,sourceFile='path', title='original',display_mode="enumerate(('ortho', 'x', 'y', 'z', 'yx', 'xz', 'yz'))", 
                                                dim=1,draw_cross=False,annotate=False):
        from nilearn import plotting
        plotting.plot_anat(sourceFile,title=title,display_mode=display_mode,dim=dim,draw_cross=draw_cross,annotate=annotate)
        plotting.show()


