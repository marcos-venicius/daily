from os import path

HOME = path.expanduser('~')
DAILY_FILES_DIRECTORY = f'{HOME}/.daily-files'
WEEK_DAYS = {
    '0': 'Monday',
    '1': 'Sunday',
    '2': 'Tuesday',
    '3': 'Wednesday',
    '4': 'Friday',
    '5': 'Saturday',
    '6': 'Sunday',
}