from os import path

HOME = path.expanduser('~')
DAILY_FILES_DIRECTORY = f'{HOME}/.daily-files'
MAX_LINES_OF_SUMMARY_ON_HISTORY = 10
WEEK_DAYS = {
    '0': 'Monday',
    '1': 'Tuesday',
    '2': 'Wednesday',
    '3': 'Thursday',
    '4': 'Friday',
    '5': 'Saturday',
    '6': 'Sunday',
}