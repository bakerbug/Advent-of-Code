class Map:
    def __init__(self):
        self.grid_size = 1000
        self.crosses = 0
        with open("inputs/day_5_inputs.txt", "r") as data_file:
            data = data_file.readlines()
        self.lines = []
        for line in data:
            line = line.rstrip("\n")
            line = line.split(" -> ")
            self.lines.append(line)

        self.grid = []
        for x in range(self.grid_size):
            row = []
            for y in range(self.grid_size):
                row.append(0)
            self.grid.append(row)

    def find_crosses(self):
        for row in self.grid:
            for column in row:
                if column > 1:
                    self.crosses += 1
        return self.crosses

    def fill_map(self):
        for line in self.lines:
            self.draw_line(line)

    def print_map(self):
        for row in self.grid:
            print(row)

    def draw_line(self, line_points):
        first_x, first_y = line_points[0].split(",")
        second_x, second_y = line_points[1].split(",")
        first_x = int(first_x)
        first_y = int(first_y)
        second_x = int(second_x)
        second_y = int(second_y)

        if first_y == second_y:
            # horizontal line
            print(f"Drawing horizontal line {line_points}")
            self.draw_horizontal_line(first_y, first_x, second_x)

        if first_x == second_x:
            # vertical line
            print(f"Drawing vertical line {line_points}")
            self.draw_vertical_line(first_x, first_y, second_y)

    def draw_horizontal_line(self, y, start, finish):
        row_index = 0
        for row in self.grid:
            if row_index == y:
                point_index = 0
                for point in row:
                    if (point_index >= start and point_index <= finish) or (point_index >= finish and point_index <= start):
                        self.grid[row_index][point_index] += 1
                    point_index += 1
            row_index += 1

    def draw_vertical_line(self, x, start, finish):
        row_index = 0
        for row in self.grid:
            if (row_index >= start and row_index <= finish) or (row_index >= finish and row_index <= start):
                column_index = 0
                for point in row:
                    if column_index == x:
                        self.grid[row_index][column_index] += 1
                    column_index += 1
            row_index += 1


if __name__ == "__main__":
    map = Map()
    map.fill_map()
    map.print_map()

    print(f"There are {map.find_crosses()} crosses.")
