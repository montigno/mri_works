##########################################################################
# mriWorks - Copyright (C) IRMAGE/INSERM, 2020
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# https://cecill.info/licences/Licence_CeCILL_V2-en.html
# for details.
##########################################################################

'''
Created on 11 feb. 2020
Modified on 28 jan. 2021
@author: omonti
'''

import subprocess
from subprocess import Popen, PIPE, call
import sys
import os


def install(command):
    p = subprocess.Popen(command, shell=True)
    p.wait()


if __name__ == '__main__':

    install('sudo apt install -y python3-venv')
    install('python3.6 -m venv ~/Apps/mri_works_venv')
    install('cp -r mri_works/ ~/Apps/mri_works_venv/')
    install('cp -r docs/ ~/Apps/mri_works_venv/')
    
    fp = open(os.path.join(os.path.expanduser('~'), '.bashrc'))
    found = False
    if '#mri_works' in fp.read():
        found = True
    if not found:
        os.system("echo '\n#mri_works' >> ~/.bashrc")    
        os.system("echo 'cmd_mw=\"source ~/Apps/mri_works_venv/bin/activate; cd ~/Apps/mri_works_venv/mri_works; python3 mri_works.py; deactivate\"' >> ~/.bashrc") 
        os.system("echo 'cmd_mw_update=\"source ~/Apps/mri_works_venv/bin/activate; cd ~/Apps/mri_works_venv/mri_works; python3 update_modules.py; deactivate\"' >> ~/.bashrc")
        os.system("echo alias mri_works=\$cmd_mw >> ~/.bashrc ")
        os.system("echo alias mri_works_update=\$cmd_mw_update >> ~/.bashrc ")
        os.system("echo '\n' >> ~/.bashrc ")
        os.system("echo 'source ~/.bashrc'")
