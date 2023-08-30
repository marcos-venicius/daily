import os
from constants import DAILY_FILES_DIRECTORY
from utils import create_daily_file_full_path

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

    def display_history(self):
        files = self.__get_daily_file_paths()

        print(files)
