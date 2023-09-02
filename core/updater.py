from shutil import which
import subprocess

from core.constants import INSTALL_PATH


class Updater:
    def __init__(self):
        pass

    def run(self):
        if which('git') is None:
            return print('\033[1;31m[!] You need git installed\033[0m')

        process = subprocess.Popen(
            ['git', 'pull', 'origin', 'main', '-f', '--allow-unrelated-histories'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=INSTALL_PATH
        )

        stdout, stderr = process.communicate()

        if process.returncode != 0:
            print('\033[1;31m[!] Something went wrong\033[0m')
            print('\033[1;37mOutput: \033[0m')
            print(stdout.decode('utf-8'))
            print('\033[1;31mError:\033[0m')
            print(stderr.decode('utf-8'))
            print()
        else:
            output = stdout.decode('utf-8')

            if output == 'Already up to date.\n':
                print('\033[1;37m[*] Daily CLI already up to date\033[0m')
            else:
                print('\033[1;32m[+] Daily CLI updated successfully\033[0m')

            print()
