from os import path

HOME = path.expanduser('~')
INSTALL_DIRECTORY = '.daily'
INSTALL_PATH = path.join(HOME, INSTALL_DIRECTORY)
OLD_INSTALL_PATH = path.join(HOME, INSTALL_DIRECTORY + '.old')
DAILY_FILES_DIRECTORY = f'{HOME}/.daily-files'
MAX_LINES_OF_SUMMARY_ON_HISTORY = 10
REPOSITORY_LOCATION = 'https://github.com/marcos-venicius/daily.git'
WEEK_DAYS = {
    '0': 'Monday',
    '1': 'Tuesday',
    '2': 'Wednesday',
    '3': 'Thursday',
    '4': 'Friday',
    '5': 'Saturday',
    '6': 'Sunday',
}