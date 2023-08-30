#!/usr/bin/env python3

from daily_history import DailyHistory
from utils import open_in_vim_editor
from functions import create_daily_files_folder_if_not_exists, create_or_open_daily_file
from arguments import ArgumentsConfigure

def create_or_open_daily_file_handler():
    daily_file_full_path = create_or_open_daily_file()

    open_in_vim_editor(daily_file_full_path)

def daily_history_handler():
    daily_history = DailyHistory()

    daily_history.display_history()

def main():
    create_daily_files_folder_if_not_exists()

    argument_configure = ArgumentsConfigure(create_or_open_daily_file_handler, 'Daily CLI')

    argument_configure.add_argument('history', 'show daily history', daily_history_handler)

    argument_configure.parse()

if __name__ == '__main__':
    main()