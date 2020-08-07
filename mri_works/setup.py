##########################################################################
# mriWorks - Copyright (C) IRMAGE/INSERM, 2020
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# https://cecill.info/licences/Licence_CeCILL_V2-en.html
# for details.
##########################################################################

'''
Created on 11 feb. 2020
@author: omonti
'''

import subprocess
from subprocess import Popen, PIPE
from packaging import version
import sys
from Config import Config

def install(command):
    p=subprocess.Popen(command,shell=True)
    p.wait()
    
def getCurrentVersion(inf):
    version = inf[inf.index('Version:')+8:]
    version=version[:version.index('\n')]
    return version.strip()
    
if __name__ == '__main__':
#     install('sudo -H pip3 install --ignore-installed PyYAML')
    pack = Config().getPathLibraries()
    for keypk,valpk in pack.items():
        version_min=''
        version_min = valpk[valpk.index('(')+1:valpk.index(')')]
        valpk=valpk.replace('('+version_min+')', '')
        try:
            lso = ("pip3 show", keypk)
            command = " ".join(lso)
            p = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
            p.wait()
            txt, error = p.communicate()
            inf = txt.decode("utf-8")
            if inf:
                if version:
                    currentVersion = getCurrentVersion(inf)
                    if version.parse(currentVersion) < version.parse(version_min):
                        answ = input('\033[93m' +'the version of '+keypk+" installed is old ("+currentVersion+"), update it to the version " + version_min +" or more ? (yes/no) :  ")
                        if answ == 'yes':
                            print('\033[93m' +'update '+keypk+' : ')
                            install(valpk)
                        else:
                            print('\033[93m' + keypk+' update canceled ')
                    else:
                        print('\033[0m' +keypk,' ....... already installed')
                else:
                    print('\033[0m' +keypk,' ....... already installed')
            else:
                print('\033[93m' +keypk,' is missing and will be installed ....')
                install(valpk)
        except:
            pass
