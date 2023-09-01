import os
from shutil import which, rmtree
import subprocess
from constants import REPOSITORY_LOCATION, INSTALL_PATH, OLD_INSTALL_PATH

class Update:
    def __init__(self):
        pass

    def __move_to_old(self):
        if os.path.isdir(INSTALL_PATH):
            os.rename(INSTALL_PATH, OLD_INSTALL_PATH)

    def __restore_old(self):
        if os.path.isdir(OLD_INSTALL_PATH):
            os.rename(OLD_INSTALL_PATH, INSTALL_PATH)

    def __clear(self):
        if os.path.isdir(INSTALL_PATH):
            rmtree(INSTALL_PATH)

    def __remove_old_copy(self):
        if os.path.isdir(OLD_INSTALL_PATH):
            rmtree(OLD_INSTALL_PATH)

    def run(self):
        if which('git') is None:
            return print('\033[1;31m[!] You need git installed\033[0m')
        
        if os.path.isdir(INSTALL_PATH):
            self.__move_to_old()

        process = subprocess.Popen(['git', 'clone', REPOSITORY_LOCATION, INSTALL_PATH], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        stdout, stderr = process.communicate()

        if process.returncode != 0:
            print('\033[1;31m[!] Something went wrong\033[0m')
            print('\033[1;37mOutput: \033[0m')
            print(stdout.decode('utf-8'))
            print('\033[1;31mError:\033[0m')
            print(stderr.decode('utf-8'))
            print()

            self.__clear()
            self.__restore_old()
        else:
            self.__remove_old_copy()

            print('\033[1;32m[+] Daily CLI updated successfully')
