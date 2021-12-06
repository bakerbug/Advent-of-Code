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
        self.diag_points = []
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
            self.draw_horizontal_line(first_y, first_x, second_x)

        elif first_x == second_x:
            # vertical line
            self.draw_vertical_line(first_x, first_y, second_y)

        else:
            # diagonal line
            self.draw_diagonal_line(first_x, first_y, second_x, second_y)

    def draw_diagonal_line(self, begin_x, begin_y, end_x, end_y):
        self.diag_points = []
        slope = (end_y - begin_y) / (end_x - begin_x)
        if slope > 0:
            pos_slope = True
        else:
            pos_slope = False

        x_points = []
        y_points = []
        line_points = []
        if begin_x < end_x:
            for x in range(begin_x, end_x + 1):
                x_points.append(x)
        if end_x < begin_x:
            for x in range(end_x, begin_x + 1):
                x_points.append(x)

        if begin_y < end_y:
            for y in range(begin_y, end_y + 1):
                y_points.append(y)
        if end_y < begin_y:
            for y in range(end_y, begin_y + 1):
                y_points.append(y)

        if pos_slope:
            self.pos_slope(x_points, y_points)
            if [begin_x, begin_y] not in self.diag_points:
                self.diag_points = []
                self.neg_slope(x_points, y_points)
        else:
            self.neg_slope(x_points, y_points)
            if [begin_x, begin_y] not in self.diag_points:
                self.diag_points = []
                self.pos_slope(x_points, y_points)

        row_id = 0
        for point in self.diag_points:
            self.grid[point[1]][point[0]] += 1

    def pos_slope(self, x_points, y_points):
        for x, y in zip(x_points, reversed(y_points)):
            self.diag_points.append([x, y])

    def neg_slope(self, x_points, y_points):
        for x, y in zip(x_points, y_points):
            self.diag_points.append([x, y])

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

    print(f"There are {map.find_crosses()} crosses.")
