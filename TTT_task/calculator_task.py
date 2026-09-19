import math


class PhoneCalculator:
    """A phone-style calculator that runs in the terminal."""

    def __init__(self):
        self.current = "0"
        self.stored = None
        self.operator = None
        self.waiting_for_operand = False
        self.expression = ""

    def format_number(self, value):
        """Format a calculated number for display."""
        if not math.isfinite(value):
            return "Error"

        value = round(value, 12)

        if value == int(value):
            return str(int(value))

        return str(value)

    def calculate(self, first, second, operator):
        """Perform the selected mathematical operation."""
        if operator == "+":
            return first + second

        if operator == "-":
            return first - second

        if operator == "×":
            return first * second

        if operator == "÷":
            if second == 0:
                return float("nan")
            return first / second

        if operator == "^":
            return math.pow(first, second)

        return second

    def input_number(self, number):
        """Enter a number."""
        if self.current == "Error" or self.waiting_for_operand:
            self.current = number
            self.waiting_for_operand = False
        else:
            if self.current == "0":
                self.current = number
            else:
                self.current += number

    def decimal(self):
        """Add a decimal point."""
        if self.current == "Error" or self.waiting_for_operand:
            self.current = "0."
            self.waiting_for_operand = False

        elif "." not in self.current:
            self.current += "."

    def choose_operator(self, operator):
        """Select an arithmetic operator."""
        try:
            value = float(self.current)
        except ValueError:
            return

        if self.stored is not None and self.operator and not self.waiting_for_operand:
            result = self.calculate(
                self.stored,
                value,
                self.operator
            )

            self.current = self.format_number(result)

            if self.current == "Error":
                return

            self.stored = result

        else:
            self.stored = value

        self.operator = operator
        self.waiting_for_operand = True

        self.expression = f"{self.current} {operator}"

    def equals(self):
        """Calculate the final result."""
        if self.stored is None or self.operator is None:
            return

        try:
            second = float(self.current)
        except ValueError:
            return

        result = self.calculate(
            self.stored,
            second,
            self.operator
        )

        if not math.isfinite(result):
            self.current = "Error"
        else:
            self.expression = (
                f"{self.format_number(self.stored)} "
                f"{self.operator} "
                f"{self.format_number(second)} ="
            )

            self.current = self.format_number(result)

        self.stored = None
        self.operator = None
        self.waiting_for_operand = True

    def clear(self):
        """Reset the calculator."""
        self.current = "0"
        self.stored = None
        self.operator = None
        self.waiting_for_operand = False
        self.expression = ""

    def delete(self):
        """Delete the last entered digit."""
        if self.waiting_for_operand or self.current == "Error":
            return

        if len(self.current) > 1:
            self.current = self.current[:-1]
        else:
            self.current = "0"

        if self.current == "-":
            self.current = "0"

    def percent(self):
        """Convert the current number to a percentage."""
        try:
            value = float(self.current)
            self.current = self.format_number(value / 100)
        except ValueError:
            self.current = "Error"

    def square_root(self):
        """Calculate the square root."""
        try:
            value = float(self.current)

            if value < 0:
                self.current = "Error"
            else:
                self.expression = f"√({self.current})"
                self.current = self.format_number(math.sqrt(value))

            self.waiting_for_operand = True

        except ValueError:
            self.current = "Error"

    def power(self):
        """Select power operation."""
        self.choose_operator("^")

    def change_sign(self):
        """Change positive number to negative and vice versa."""
        if self.current == "0" or self.current == "Error":
            return

        if self.current.startswith("-"):
            self.current = self.current[1:]
        else:
            self.current = "-" + self.current

    def display(self):
        """Display the calculator screen."""
        print("\033[2J\033[H", end="")

        print("╔══════════════════════════════╗")
        print("║       UDAY  CALCULATOR       ║")
        print("╠══════════════════════════════╣")
        print(f"║ {self.expression:>28} ║")
        print(f"║ {self.current:>28} ║")
        print("╠══════════════════════════════╣")
        print("║   AC    DEL     %      ÷     ║")
        print("║   7      8      9      ×     ║")
        print("║   4      5      6      −     ║")
        print("║   1      2      3      +     ║")
        print("║   √      0      .      =     ║")
        print("║   xʸ     ±                   ║")
        print("╚══════════════════════════════╝")
        print()
        print("Enter a button:")
        print(
            "  0-9 | + | - | * | / | % | . | "
            "sqrt | power | +/- | = | ac | del | exit"
        )

    def process_command(self, command):
        """Process a user command."""
        command = command.lower().strip()

        if command == "exit":
            return False

        if command == "ac":
            self.clear()

        elif command == "del":
            self.delete()

        elif command == "%":
            self.percent()

        elif command == "sqrt":
            self.square_root()

        elif command == "power":
            self.power()

        elif command in ("+/-", "±"):
            self.change_sign()

        elif command == "=":
            self.equals()

        elif command == ".":
            self.decimal()

        elif command in ("+", "-", "*", "/"):
            operators = {
                "+": "+",
                "-": "-",
                "*": "×",
                "/": "÷"
            }

            self.choose_operator(operators[command])

        elif command.isdigit():
            for digit in command:
                self.input_number(digit)

        else:
            print("\nInvalid input.")
            input("Press Enter to continue...")

        return True

    def run(self):
        """Start the calculator."""
        while True:
            self.display()

            command = input("\n>>> ")

            if not self.process_command(command):
                print("\nThank you for using uday Calculator!")
                break


def main():
    calculator = PhoneCalculator()
    calculator.run()


if __name__ == "__main__":
    main()

