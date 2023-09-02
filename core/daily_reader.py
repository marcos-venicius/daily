import os


class DailyReader:
    def __init__(self, path: str = ''):
        self.path = path
        self.files_cache = {}

    def __file_exists(self):
        return os.path.isfile(self.path)

    def __get_file_lines(self) -> list[str]:
        if not self.__file_exists():
            raise Exception('This file does not exists')

        if self.path in self.files_cache:
            return self.files_cache[self.path]

        lines = []

        with open(self.path, 'r') as file:
            lines = file.readlines()
            file.close()

        self.files_cache[self.path] = lines

        return lines

    def update_path(self, path: str):
        self.path = path

    def read_between_tokens(self, starts_at: str, ends_at: str, number_of_lines=10, strip=False) -> str:
        file = self.__get_file_lines()
        reading = False
        lines = []

        for line in file:
            if not reading and line.startswith(starts_at):
                reading = True
                continue
            elif line.startswith(ends_at) or number_of_lines == 0:
                break

            if reading:
                if strip:
                    if len(line.strip()) == 0:
                        continue
                    line = line.strip() + '\n'

                number_of_lines -= 1
                lines.append(line)

        return ''.join(lines)
