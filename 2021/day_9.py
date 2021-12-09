class Mapper:
    def __init__(self):
        with open("inputs/day_9_input.txt", "r") as data_file:
            self.raw_data = data_file.readlines()
        self.y_length = len(self.raw_data)
        txt_input = []
        self.input = []
        self.low_map = []
        self.low_list = []
        self.basin_map = []
        self.basin_list = []
        self.this_basin = []
        self.size_list = []
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
            self.basin_map.append(map_row)

    def find_basins(self):
        for low_point in self.low_list:
            self.this_basin = [low_point]
            print(f"Scanning low point at {low_point}")
            self.map_basin(low_point)
            self.basin_list.append(self.this_basin)
            print(f"Basin at {low_point} has a size of {len(self.this_basin)}")
            self.size_list.append(len(self.this_basin))

    def find_biggest_sizes(self):
        first = max(self.size_list)
        self.size_list.remove(first)
        second = max(self.size_list)
        self.size_list.remove(second)
        thrid = max(self.size_list)

        print(f"The biggest basins have a size of {first}, {second}, and {thrid}")
        answer = first * second * thrid
        print(f"The answer is {answer}")



    def map_basin(self, spot):
        found_spot = False
        north = [spot[0] - 1, spot[1]]
        east = [spot[0], spot[1] + 1]
        south = [spot[0] + 1, spot[1]]
        west = [spot[0], spot[1] - 1]

        try:
            if self.input[north[0]][north[1]] < 9 and north not in self.this_basin and north[0] >= 0 and north[1] >= 0:
                print(f"Found North {self.input[north[0]][north[1]]} at {north[1]}, {north[0]}")
                found_spot = True
                self.this_basin.append([north[0], north[1]])
                self.map_basin([north[0], north[1]])
        except IndexError:
            pass

        try:
            if self.input[east[0]][east[1]] < 9 and east not in self.this_basin and east[0] >= 0 and east[1] >= 0:
                print(f"Found East {self.input[east[0]][east[1]]} at {east[1]}, {east[0]}")
                found_spot = True
                self.this_basin.append([east[0], east[1]])
                self.map_basin([east[0], east[1]])
        except IndexError:
            pass

        try:
            if self.input[south[0]][south[1]] < 9 and south not in self.this_basin and south[0] >= 0 and south[1] >= 0:
                print(f"Found south {self.input[south[0]][south[1]]} at {south[1]}, {south[0]}")
                found_spot = True
                self.this_basin.append([south[0], south[1]])
                self.map_basin([south[0], south[1]])
        except IndexError:
            pass

        try:
            if self.input[west[0]][west[1]] < 9 and west not in self.this_basin and west[0] >= 0 and west[1] >= 0:
                print(f"Found west {self.input[west[0]][west[1]]} at {west[1]}, {west[0]}")
                found_spot = True
                self.this_basin.append([west[0], west[1]])
                self.map_basin([west[0], west[1]])
        except IndexError:
            pass

        return found_spot









    def find_low_points(self):
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
                    self.low_list.append([y_index, x_index])

    def risk_calculator(self):

        risk = 0
        for y_index in range(self.y_length):
            for x_index in range(self.x_length):
                if type(self.low_map[y_index][x_index]) == int:
                    risk += self.low_map[y_index][x_index] + 1

        print(f"Risk level is {risk}")

    def print_basins(self):

        for row in self.basin_map:
            print(row)


if __name__ == "__main__":
    map = Mapper()
    print(f"Map is {map.x_length} by {map.y_length}")
    map.find_low_points()
    map.risk_calculator()
    map.find_basins()
    map.find_biggest_sizes()

