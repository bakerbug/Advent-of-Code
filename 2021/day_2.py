class Position:
    def __init__(self):
        data_file = open("inputs/day_2_input.txt", "r")
        self.position_data = data_file.readlines()
        data_file.close()
        self.horizontal = 0
        self.depth = 0

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

    def follow_course(self):
        for movement in self.position_data:
            self.plot_movement(movement)

        location = self.horizontal * self.depth

        return location


if __name__ == "__main__":
    course = Position()

    print(f"Location is {course.follow_course()}")
