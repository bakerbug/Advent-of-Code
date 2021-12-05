class Position:
    def __init__(self):
        data_file = open("inputs/day_2_input.txt", "r")
        # data_file = open("inputs/sample.txt", "r")
        self.position_data = data_file.readlines()
        data_file.close()
        self.horizontal = 0
        self.depth = 0
        self.aim = 0

    def plot_movement(self, movement):
        change = movement.split()
        direction = change[0]
        distance = int(change[1])

        if direction == "forward":
            self.horizontal += distance
        if direction == "backward":
            self.horizontal -= distance
        if direction == "down":
            self.depth += distance
        if direction == "up":
            self.depth -= distance

    def plot_aim_movement(self, movement):
        change = movement.split()
        direction = change[0]
        distance = int(change[1])

        if direction == "forward":
            self.horizontal += distance
            if self.aim != 0:
                self.depth += distance * self.aim
        if direction == "backward":
            self.horizontal -= distance
            if self.aim != 0:
                self.depth -= distance * self.aim
        if direction == "down":
            self.aim += distance
        if direction == "up":
            self.aim -= distance

    def follow_course(self):
        for movement in self.position_data:
            self.plot_movement(movement)

        location = self.horizontal * self.depth

        return location

    def follow_aim_course(self):
        for movement in self.position_data:
            self.plot_aim_movement(movement)

        print(f"Location is {self.horizontal} and depth is {self.depth}")
        location = self.horizontal * self.depth

        return location


if __name__ == "__main__":
    course = Position()

    # print(f"Location is {course.follow_course()}")
    print(f"Location is {course.follow_aim_course()}")
