# from os.path import join as opj
# import os
# import json
# from nipype.interfaces.fsl import (BET, ExtractROI, FAST, FLIRT, ImageMaths,
#                                    MCFLIRT, SliceTimer, Threshold)
# from nipype.interfaces.utility import IdentityInterface
# from nipype.interfaces.io import SelectFiles, DataSink
# from nipype.algorithms.rapidart import ArtifactDetect
from nipype.interfaces.spm import Smooth
from nipype import Workflow, Node

class smoothing():
    def __init__(self,fwhm=[4,8]):
        smooth = Node(Smooth(), name="smooth")
        smooth.iterables = ("fwhm", fwhm)