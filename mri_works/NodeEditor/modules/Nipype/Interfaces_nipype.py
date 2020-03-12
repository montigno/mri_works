from nipype.interfaces.spm import Smooth
from nipype import Workflow, Node


class smoothing():
    def __init__(self, fwhm=[4, 8]):
        smooth = Node(Smooth(), name="smooth")
        smooth.iterables = ("fwhm", fwhm)
