# run from git repo root folder
from time import sleep
import os
import subprocess
from pathlib import *
import shutil
from loguru import logger

os.chdir('..')
while True:
    logger.success('Pulling from git...')
    git_output = subprocess.check_output('git pull'.split(' ')).decode()
    if 'Already up to date.' in git_output:
        logger.success('Not running tests, as repository is up to date.')

    else:
        python_dir = subprocess.check_output('which python'.split(' ')).decode('utf-8')[:-1]

        site_packages = f'{os.path.join(*os.path.split(python_dir)[:-1])}/Lib/site-packages/'
        backslash = '\\'
        folder = f'C:{str(WindowsPath(site_packages+"pygns3/"))[2:]}'.replace('\\\\', '\\')
        print(folder)

        logger.success(f'Removing old site-package from {folder}...')
        try:
            shutil.rmtree(folder)
        except Exception:
            pass


        logger.success('Adding to site-packages')
        subprocess.run(f'cp -r pygns3 {folder}'.split(' '))

        os.chdir('test')
        print(os.listdir('.'))


        logger.success('Executing test...')
        pytest_command = open('./run.sh').read()
        subprocess.run(pytest_command.strip().split(' '))
        os.chdir('..')

    logger.success('\n\n\n')
    sleep(10)

