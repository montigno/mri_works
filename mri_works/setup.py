##########################################################################
# mriWorks - Copyright (C) IRMAGE/INSERM, 2020
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# https://cecill.info/licences/Licence_CeCILL_V2-en.html
# for details.
##########################################################################

'''
Created on 11 feb. 2020
Modified on 13 aug. 2020
@author: omonti
'''

import subprocess
from subprocess import Popen, PIPE
import sys


def install(command):
    p=subprocess.Popen(command,shell=True)
    p.wait()

    
if __name__ == '__main__':
    install('pip install --upgrade pip')
    install('pip3 install --ignore-installed PyYAML')
    from Config import Config
    pack = Config().getPathLibraries()
    for keypk,valpk in pack.items():
        try:
            print('\033[93m'+'checking ',keypk,end=' : ')
            print('\033[0m')
            install(valpk)
            print('\033[0m')
        except Exception as e:
            print('error : ', e)
