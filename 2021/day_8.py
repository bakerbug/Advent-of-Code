# Unique
ONE = (2, 5)  # 2
FOUR = (2, 3, 4, 5)  # 4
SEVEN = (2, 5, 6)  # 3
EIGHT = (0, 1, 2, 3, 4, 5, 6)  # 7

# Common
TWO = (0, 1, 3, 5, 6)  # 5
THREE = (0, 2, 3, 5, 6)  # 5
FIVE = (0, 2, 3, 4, 6)  # 5
SIX = (0, 1, 2, 3, 4, 6)  # 6
NINE = (0, 2, 3, 4, 5, 6)  # 6
ZERO = (0, 1, 2, 4, 5, 6)  # 6

U_LENGTHS = {1: 2, 4: 4, 7: 3, 8: 7}
C_LENGTHS = {2: 5, 3: 5, 5: 5, 6: 6, 9: 6, 0: 6}


class Decoder:
    def __init__(self):
        with open("inputs/day_8_input.txt", "r") as data_file:
            self.raw_data = data_file.readlines()

    def q_and_d(self):
        total = 0
        for number in self.raw_data:
            wires, output = number.split("|")
            numbers = output.split()
            for number in numbers:
                if len(number) == 2 or len(number) == 4 or len(number) == 3 or len(number) == 7:
                    total += 1
        print(total)


if __name__ == "__main__":
    digits = Decoder()
    digits.q_and_d()
