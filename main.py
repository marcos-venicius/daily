#!/usr/bin/env python3

from core.updater import Updater
from core.daily_history import DailyHistory
from core.utils import open_in_vim_editor
from core.functions import create_daily_files_folder_if_not_exists, create_or_open_daily_file
from core.arguments import ArgumentsConfigure


def create_or_open_daily_file_handler():
    daily_file_full_path = create_or_open_daily_file()

    open_in_vim_editor(daily_file_full_path)


def main():
    updater = Updater()
    daily_history = DailyHistory()

    create_daily_files_folder_if_not_exists()

    argument_configure = ArgumentsConfigure(
        create_or_open_daily_file_handler, 'Daily CLI'
    )

    argument_configure.add_argument(
        'history', 'show daily history', daily_history.display_history
    )
    argument_configure.add_argument(
        'today', 'today daily in VIEW MODE', daily_history.display_today
    )
    argument_configure.add_argument('update', 'update the CLI', updater.run)

    argument_configure.parse()


if __name__ == '__main__':
    main()
