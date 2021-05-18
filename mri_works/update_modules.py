import subprocess
from subprocess import Popen, PIPE


def install(command):
    p = subprocess.Popen(command, shell=True)
    p.wait()

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