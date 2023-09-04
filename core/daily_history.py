import os
from core.constants import DAILY_FILES_DIRECTORY, MAX_LINES_OF_SUMMARY_ON_HISTORY
from core.utils import extract_day_and_date_from_file_name, get_date_formatted, create_daily_file_full_path
from core.daily_reader import DailyReader
from core.tokens import Tokens


class DailyHistory:
    def __init__(self):
        self.daily_reader = DailyReader()

    def __mount_path_until_file(self, filename) -> str:
        return os.path.join(DAILY_FILES_DIRECTORY, filename)

    def __get_daily_file_paths(self) -> list[str]:
        paths: list[str] = []

        for filename in os.listdir(DAILY_FILES_DIRECTORY):
            if not filename.startswith('.'):
                path = self.__mount_path_until_file(filename)

                paths.append(path)

        return paths

    def __sort_daily(self, date: str) -> int:
        return int(''.join(date.split('-')[::-1]))

    def display_today(self):
        today_daily_path = create_daily_file_full_path()

        self.daily_reader.update_path(today_daily_path)

        if not os.path.isfile(today_daily_path):
            print("\033[1;33m[!]\033[0m You haven't created your daily yet")
            return exit(-1)

        weekday, date = extract_day_and_date_from_file_name(today_daily_path)
        summary = self.daily_reader.read_between_tokens(
            starts_at=Tokens.SUMMARY,
            ends_at=Tokens.NOTES,
            number_of_lines=-1
        )

        print()
        print(f'\033[1;36mToday\033[0m\t\t \033[1;34m{weekday}, {date}\033[0m')
        print()
        print(f'\033[2;37m{summary}\033[0m')
        print()

    def display_history(self):
        files = self.__get_daily_file_paths()

        today = get_date_formatted()

        files_with_metadata = []

        for file in files:
            weekday, date = extract_day_and_date_from_file_name(file)

            files_with_metadata.append((file, weekday, date))

        files_with_metadata = sorted(
            files_with_metadata, key=lambda file: self.__sort_daily(file[2])
        )

        for file in files_with_metadata:
            self.daily_reader.update_path(file[0])
            data = self.daily_reader.read_between_tokens(
                starts_at=Tokens.SUMMARY,
                ends_at=Tokens.NOTES,
                number_of_lines=MAX_LINES_OF_SUMMARY_ON_HISTORY,
                strip=True
            )
            weekday, date = file[1], file[2]

            header = f'{date}, {weekday}\t \033[1;34m[first {MAX_LINES_OF_SUMMARY_ON_HISTORY} summary lines]\n\033[0m'

            if today == date:
                header = f"\033[1;36mToday\033[0m - {header}"

            print(header)
            if len(data) == 0:
                print('\033[1;33m(Without summary)\033[0m')
            else:
                print(f'\033[2;37m{data}\033[0m')
            print()
