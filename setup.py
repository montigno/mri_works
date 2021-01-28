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
import os


def install(command):
    p = subprocess.Popen(command, shell=True)
    p.wait()


if __name__ == '__main__':
    # install('python3 -m pip install --upgrade pip')
#     install('pip install --upgrade pip')
    install('python3.6 -m venv ~/Apps/python_env_2')
    install ('cp -r mri_works/ ~/Apps/python_env_2/')
    install ('cp -r docs/ ~/Apps/python_env_2/')
    install('cd ~/Apps/python_env_2')
    install('source bin/activate')
    install('pip install --upgrade pip')
    install('pip3 install --ignore-installed PyYAML')
    from Config import Config
    pack = Config().getPathLibraries()
    for keypk, valpk in pack.items():
        try:
            print('\033[93m'+'checking ', keypk, end=' : ')
            print('\033[0m')
            install(valpk)
            print('\033[0m')
        except Exception as e:
            print('error : ', e)
    install('deactivate')       
    os.system("echo '\n#mri_works' >> ~/.bashrc")    
    os.system("echo 'cmd_mw=\"source ~/Apps/python_env_2/bin/activate; cd ~/Apps/python_env_2/mri_works; python3 mri_works.py; deactivate\"' >> ~/.bashrc")    
    os.system("echo alias mri_works=\$cmd_mw >> ~/.bashrc ")
    os.system("echo '\n' >> ~/.bashrc ")
    os.system("echo 'source ~/.bashrc'")
