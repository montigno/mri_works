class smoothing():
    def __init__(self, fwhm=[4, 8]):
        from nipype.interfaces.spm import Smooth
        from nipype import Workflow, Node
        smooth = Node(Smooth(), name="smooth")
        smooth.iterables = ("fwhm", fwhm)
