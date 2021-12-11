class Octopi:
    def __init__(self):
        self.input = []
        self.map = []
        self.total_flashes = 0
        self.again_count = 0
        with open("inputs/day_11_input.txt", "r") as data_file:
            input = data_file.readlines()
            for line in input:
                digits = []
                line = line.rstrip("\n")
                line = list(line)
                for digit in line:
                    digits.append(int(digit))
                self.input.append(digits)
                self.map.append([None, None, None, None, None, None, None, None, None, None])

    def print_map(self):
        for line in self.input:
            print(line)
        print("\n")

    def process_octopus(self, x_pos, y_pos):
        flash = False
        n = [y_pos - 1, x_pos]
        ne = [y_pos - 1, x_pos + 1]
        e = [y_pos, x_pos + 1]
        se = [y_pos + 1, x_pos + 1]
        s = [y_pos + 1, x_pos]
        sw = [y_pos + 1, x_pos - 1]
        w = [y_pos, x_pos - 1]
        nw = [y_pos - 1, x_pos - 1]

        if self.input[y_pos][x_pos] > 9:
            self.total_flashes += 1
            self.input[y_pos][x_pos] = 0
            neighbors = [n, ne, e, se, s, sw, w, nw]
            for neighbor in neighbors:
                try:
                    if neighbor[0] >= 0 and neighbor[1] >= 0 and self.input[neighbor[0]][neighbor[1]] != 0:
                        self.input[neighbor[0]][neighbor[1]] += 1
                        flash = True
                except IndexError:
                    pass
        return flash

    def step_swarm(self):
        for step in range(100):
            y_index = 0
            for row in self.input:
                x_index = 0
                for octupus in row:
                    self.input[y_index][x_index] += 1
                    x_index += 1
                y_index += 1
            self.process_flashes()

    def process_flashes(self):
        keep_going = True
        while keep_going:
            keep_going = False
            print(f"Going again! {self.again_count}")
            self.again_count += 1
            y_index = 0
            for row in self.input:
                x_index = 0
                for octupus in row:
                    flash_detected = self.process_octopus(x_index, y_index)
                    if flash_detected:
                        keep_going = True
                    x_index += 1
                y_index += 1
            self.print_map()


if __name__ == "__main__":
    octo = Octopi()
    octo.print_map()
    octo.step_swarm()
    octo.process_flashes()
    octo.print_map()
    print(f"Total Flashes: {octo.total_flashes}")
