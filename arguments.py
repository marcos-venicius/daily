import argparse

class ArgumentsConfigure:
    def __init__(self, description: str):
        self.parser = argparse.ArgumentParser(description=description)

    def add_argument(self, name: str, help: str) -> None:
        self.parser.add_argument(f'--{name}', action="store_true", help=help)

    def parse(self):
        return self.parser.parse_args()