import os
from core.constants import DAILY_FILES_DIRECTORY
from core.utils import create_daily_file_full_path, get_week_display_name, get_date_formatted


def create_daily_files_folder_if_not_exists() -> None:
    if os.path.isdir(DAILY_FILES_DIRECTORY):
        return
    
    os.mkdir(DAILY_FILES_DIRECTORY)

def create_or_open_daily_file() -> str:
    """
    returns the path to the file created
    """

    full_path = create_daily_file_full_path()
    date_formatted = get_date_formatted()
    week_day = get_week_display_name()

    header = f'DAILY: {week_day}, {date_formatted}'

    if not os.path.isfile(full_path):
        with open(full_path, 'w') as file:
            file.write(header)
            file.write('\n\n')
            file.write('In the morning:\n\n')
            file.write('In the afternoon:\n\n')
            file.write('Summary:\n\n')
            file.write('Notes:\n\n')
            file.close()

    return full_path