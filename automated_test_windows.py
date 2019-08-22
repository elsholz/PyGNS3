# run from git repo root folder
from time import sleep
import os
import subprocess
import shutil

while True:
    subprocess.run('git pull'.split(' '))
    subprocess.run('which python > .python_dir.txt'.split(' '))
    python_dir = open('./.python_dir.txt').read()
    shutil.rmtree(os.path.join(python_dir, 'Lib', 'site-packages', 'pygns3'))
    subprocess.run(f'cp pygns3 {os.path.join(python_dir, "Lib", "site-packages", "pygns3")}'.split(' '))
    os.chdir('test')
    subprocess.run('run.sh'.split(' '))
    os.chdir('..')

    sleep(60)

