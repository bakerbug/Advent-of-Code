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

U_LENGTHS = {1: 2, 4: 4, 7: 3, 8: 7}  # number: length
LENGTHS = {2: 5, 3: 5, 5: 5, 6: 6, 9: 6, 0: 6, 1: 2, 4: 4, 7: 3, 8: 7}


class Decoder:
    def __init__(self):
        with open("inputs/day_8_input.txt", "r") as data_file:
            self.raw_data = data_file.readlines()
        self.input = []
        for line in self.raw_data:
            self.input.append(line.strip("\n"))
        self.reset()

    def reset(self):
        self.digit_map = {}
        self.segment_map = {"1": set(), "2": set(), "3": set(), "4": set(), "5": set(), "6": set(), "7": set(), "8": set(), "9": set(), "0": set()}
        self.retry_patterns = []

    def q_and_d(self):
        total = 0
        for number in self.input:
            wires, output = number.split("|")
            numbers = output.split()
            for number in numbers:
                if len(number) == 2 or len(number) == 4 or len(number) == 3 or len(number) == 7:
                    total += 1
        print(total)

    def accumulator(self):
        grand_total = 0
        for display in self.input:
            # print(f"{display} length: {len(display)}")
            self.reset()
            readout = ""
            wires, output = display.split("|")
            output = output.split()
            # print(f"There are {len(output)} digits to test.")
            wires = wires.split()
            for number in wires:
                self.id_unique_wires(number)

            # print(f"Output: {output}")
            for number in wires:
                if number not in self.digit_map:
                    self.id_common_wires(number)

            for number in self.retry_patterns:
                self.id_common_wires(number)

            for digit in output:
                digit_set = set(digit)
                guesses = list(self.segment_map.keys())
                wires = list(self.segment_map.values())

                for index in range(10):
                    if digit_set == wires[index]:
                        readout = readout + guesses[index]
            print(f"Readout: {readout}")
            grand_total += int(readout)

        print(f"The final answer is {grand_total}")

    def id_unique_wires(self, pattern):
        if len(pattern) == 7:
            self.digit_map.update({pattern: 7})
            self.segment_map["8"] = set(pattern)
            # print(f"Found {pattern} as 8")
        elif len(pattern) == 3:
            self.digit_map.update({pattern: 7})
            self.segment_map["7"] = set(pattern)
            # print(f"Found {pattern} as 7")
        elif len(pattern) == 4:
            self.digit_map.update({pattern: 4})
            self.segment_map["4"] = set(pattern)
            # print(f"Found {pattern} as 4")
        elif len(pattern) == 2:
            self.digit_map.update({pattern: 1})
            self.segment_map["1"] = set(pattern)
            # print(f"Found {pattern} as 1")

    def id_common_wires(self, pattern):
        pat_len = len(pattern)
        segments = set(pattern)

        # Nine has 1, 4, 7 and not 8, + 1 seg
        if len(self.segment_map["1"].intersection(segments)) == LENGTHS[1] and \
            len(self.segment_map["4"].intersection(segments)) == LENGTHS[4] and \
            len(self.segment_map["7"].intersection(segments)) == LENGTHS[7] and\
            pat_len == LENGTHS[9]:
            self.segment_map["9"] = set(pattern)
            self.digit_map.update({pattern: 9})
            # print(f"Found {pattern} as 9")
            return

        # Five has 9 minus 1 seg and has 1 minus 1 seg
        if len(self.segment_map["9"].intersection(segments)) == LENGTHS[9] - 1 and \
            len(self.segment_map["1"].intersection(segments)) == LENGTHS[1] - 1 and \
            pat_len == LENGTHS[5]:
            self.segment_map["5"] = set(pattern)
            self.digit_map.update({pattern: 5})
            # print(f"Found {pattern} as 5")
            return

        # Zero has 8 - 1 segment, has 7, has 1 (Union with 4 + 3 segments)
        if len(self.segment_map["8"].intersection(segments)) == LENGTHS[8] - 1 and \
            len(self.segment_map["7"].intersection(segments)) == LENGTHS[7] and \
            len(self.segment_map["1"].intersection(segments)) == LENGTHS[1] and \
            len(self.segment_map["4"].union(segments)) == LENGTHS[4] + 3 and \
            pat_len == LENGTHS[0]:
            self.segment_map["0"] = set(pattern)
            self.digit_map.update({pattern: 0})
            # print(f"Found {pattern} as 0")
            return

        # Three has 9 - 1 segment, has 7, has 1
        if len(self.segment_map["9"].intersection(segments)) == LENGTHS[9] - 1 and \
            len(self.segment_map["7"].intersection(segments)) == LENGTHS[7] and \
            len(self.segment_map["1"].intersection(segments)) == LENGTHS[1] and \
            pat_len == LENGTHS[3]:
            self.segment_map["3"] = set(pattern)
            self.digit_map.update({pattern: 3})
            # print(f"Found {pattern} as 3")
            return

        # Needs to have found 5
        # Six has a 5, has an 8 minus 1 segment
        if len(self.segment_map["5"]) != 0 and \
            len(self.segment_map["5"].intersection(segments)) == LENGTHS[5] and \
            len(self.segment_map["8"].intersection(segments)) == LENGTHS[8] - 1 and \
            pat_len == LENGTHS[6]:
            self.segment_map["6"] = set(pattern)
            self.digit_map.update({pattern: 6})
            # print(f"Found {pattern} as 6")
            return

        # Two, If we already found 6, then this is all that is left
        if len(self.segment_map["6"]) != 0 and \
            pat_len == LENGTHS[2]:
            self.segment_map["2"] = set(pattern)
            self.digit_map.update({pattern: 2})
            # print(f"Found {pattern} as 2")
            return

        self.retry_patterns.append(pattern)


if __name__ == "__main__":
    digits = Decoder()
    # digits.q_and_d()
    digits.accumulator()
