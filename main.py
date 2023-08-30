#!/usr/bin/env python3

from utils import create_daily_file_full_path, open_in_vim_editor
from functions import create_daily_files_folder_if_not_exists, create_or_open_daily_file
from arguments import ArgumentsConfigure

def main():
    create_daily_files_folder_if_not_exists()

    argument_configure = ArgumentsConfigure('Daily CLI')

    argument_configure.add_argument('history', 'show daily history')

    args = argument_configure.parse()

    daily_file_full_path = create_daily_file_full_path()

    if not args.history:
        daily_file_full_path = create_or_open_daily_file()

        open_in_vim_editor(daily_file_full_path)

if __name__ == '__main__':
    main()