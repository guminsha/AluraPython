import re


class PhoneBrasil:
    def __init__(self, number) -> None:
        if self.validating_number(number):
            self.number = number
        else:
            raise ValueError("Invalid Number")

    def validating_number(self, number):
        phone_pattern = re.compile("(\d{2})9(\d{4})(\d{4})")
        match = phone_pattern.match(number)

        if match:
            return True
        else:
            return False

    def formating_number(self):
        if len(self.number) == 11:
            return f"({self.number[:2]}){self.number[2:7]}-{self.number[7:]}"

    def __str__(self) -> str:
        return self.formating_number()
