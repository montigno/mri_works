##########################################################################
# mriWorks - Copyright (C) IRMAGE/INSERM, 2020
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# https://cecill.info/licences/Licence_CeCILL_V2-en.html
# for details.
##########################################################################

import cProfile
import re
import sys
from mri_works import Project_Irmage
from PyQt5.QtWidgets import QApplication



if __name__ == '__main__':

    app = QApplication(sys.argv)
    cProfile.run(Project_Irmage())
    if imageViewer.state:
        sys.exit(app.exec_())