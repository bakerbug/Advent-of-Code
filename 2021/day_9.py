class Mapper:
    def __init__(self):
        with open("inputs/day_9_input.txt", "r") as data_file:
            self.raw_data = data_file.readlines()
        self.y_length = len(self.raw_data)
        txt_input = []
        self.input = []
        self.low_map = []
        for line in self.raw_data:
            txt_input.append(list(line.strip("\n")))

        for line in txt_input:
            self.x_length = len(line)
            input_row = []
            map_row = []
            for item in line:
                input_row.append(int(item))
                map_row.append(None)
            self.input.append(input_row)
            self.low_map.append(map_row)

    def scanner(self):
        for y_index in range(self.y_length):
            for x_index in range(self.x_length):
                previous_x = x_index - 1
                next_x = x_index + 1
                previous_y = y_index - 1
                next_y = y_index + 1

                try:
                    up = self.input[previous_y][x_index]
                except IndexError:
                    up = 10
                    # print(f"Up border at {x_index}, {previous_y}")

                try:
                    down = self.input[next_y][x_index]
                except IndexError:
                    down = 10
                    # print(f"Down border at {x_index}, {next_y}")

                try:
                    left = self.input[y_index][previous_x]
                except IndexError:
                    left = 10
                    # print(f"Left border at {previous_x}, {y_index}")

                try:
                    right = self.input[y_index][next_x]
                except IndexError:
                    right = 10
                    # print(f"Right border at {next_x}, {y_index}")

                if self.input[y_index][x_index] < up and self.input[y_index][x_index] < down and self.input[y_index][x_index] < left and self.input[y_index][x_index] < right:
                    print(f"Found low point of {self.input[y_index][x_index]} at {x_index}, {y_index}")
                    self.low_map[y_index][x_index] = self.input[y_index][x_index]

    def risk_calculator(self):

        risk = 0
        for y_index in range(self.y_length):
            for x_index in range(self.x_length):
                if type(self.low_map[y_index][x_index]) == int:
                    risk += self.low_map[y_index][x_index] + 1

        print(f"Risk level is {risk}")


if __name__ == "__main__":
    map = Mapper()
    print(f"Map is {map.x_length} by {map.y_length}")
    map.scanner()
    map.risk_calculator()
