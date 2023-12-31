import os
from datetime import date
from subprocess import Popen

from core.constants import WEEK_DAYS, DAILY_FILES_DIRECTORY
from core.tokens import Tokens


def get_week_display_name() -> str:
    week_day_number = date.today().weekday()

    return WEEK_DAYS[str(week_day_number)]


def get_date_formatted() -> str:
    current_date = date.today()
    current_date = str(current_date).split('-')
    current_date = current_date[::-1]

    return '-'.join(current_date)


def create_daily_file_full_path() -> str:
    """
    create daily file name with full path to it
    """

    current_date = get_date_formatted()

    week_day_as_string = get_week_display_name().lower()

    filename = f'{week_day_as_string}-{current_date}.txt'

    return os.path.join(DAILY_FILES_DIRECTORY, filename)


def extract_day_and_date_from_file_name(path: str) -> (str, str):
    """
    Returns:
        (filename, date) 
    """

    split = path.split('/')
    filename = split[len(split) - 1]
    filename = filename[0:filename.index('.')]

    day, *date = filename.split('-')

    day = day.capitalize()
    date = '-'.join(date)

    return (day, date)


def open_in_vim_editor(file_path: str) -> None:
    process = Popen(['vim', file_path])

    try:
        process.wait()
    except:
        process.terminate()
