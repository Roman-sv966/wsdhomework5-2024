# calculator/plugins/multiply_command.py
from decimal import Decimal
from calculator.command import Command
from calculator.command_registry import register_command

class MultiplyCommand(Command):
    def __init__(self, a: Decimal, b: Decimal):
        self.a = a
        self.b = b

    def execute(self) -> Decimal:
        return self.a * self.b

register_command("multiply", MultiplyCommand)