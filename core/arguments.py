import argparse


class ArgumentsConfigure:
    def __init__(self, execute_when_empty, description: str):
        self.parser = argparse.ArgumentParser(description=description)
        self.relations = {}
        self.execute_when_empty = execute_when_empty

    def add_argument(self, name: str, help: str, handler) -> None:
        """
        Add a new argument related to a handler

        Args:
            name (str): the name of the argument, example: help, version
            help (str): the command help
            handler: the method that will be executed when this argument is passed

        Returns:
            None
        """

        self.parser.add_argument(f'--{name}', action="store_true", help=help)
        self.relations[name] = handler

    def parse(self):
        arguments = self.parser.parse_args()

        if not any(vars(arguments).values()):
            self.execute_when_empty()
            return

        for argument in arguments.__dict__:
            if arguments.__dict__[argument] and argument in self.relations:
                self.relations[argument]()
                return
