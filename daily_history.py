import os
from constants import DAILY_FILES_DIRECTORY, MAX_LINES_OF_SUMMARY_ON_HISTORY
from utils import extract_day_and_date_from_file_name, get_date_formatted

class DailyHistory:
    def __init__(self) -> None:
        pass

    def __mount_path_until_file(self, filename) -> str:
        return os.path.join(DAILY_FILES_DIRECTORY, filename)

    def __get_daily_file_paths(self) -> list[str]:
        paths: list[str] = []

        for filename in os.listdir(DAILY_FILES_DIRECTORY):
            if not filename.startswith('.'):
                path = self.__mount_path_until_file(filename)

                paths.append(path)

        return paths

    def __get_daily_data(self, path: str) -> str:
        lines: list[str] = []

        with open(path, 'r') as file:
            getting_lines = False
            lines_count = MAX_LINES_OF_SUMMARY_ON_HISTORY

            for line in file:
                if line.startswith('Summary:'):
                    getting_lines = True
                    continue
                elif line.startswith('Notes:') or lines_count <= 0:
                    file.close()
                    break

                if getting_lines:
                    lines_count -= 1
                    line = f'\t {line.strip()}'
                    lines.append(line)

        lines = [line for line in lines if len(line.strip()) != 0]

        return '\n'.join(lines)

    def display_history(self):
        files = self.__get_daily_file_paths()

        today = get_date_formatted()

        files_with_metadata = []

        for file in files:
            weekday, date = extract_day_and_date_from_file_name(file)

            files_with_metadata.append((file, weekday, date))

        files_with_metadata = sorted(files_with_metadata, key=lambda file: file[2])

        for file in files_with_metadata:
            data = self.__get_daily_data(file[0])
            weekday, date = file[1], file[2]

            header = f'{weekday}, {date} \033[1;33m[first {MAX_LINES_OF_SUMMARY_ON_HISTORY} summary lines]\n\033[0m'

            if today == date:
                header = f"\033[1;36mToday\033[0m - {header}"

            print(header)
            print('\033[2;37m', data, '\033[0m')
            print()
