class Fish:
    def __init__(self, timer: int):
        self.timer = timer

    def age_fish(self):
        if self.timer == 0:
            self.timer = 6
            return True
        else:
            self.timer -= 1
            return False


class School:
    def __init__(self):
        self.data = []
        self.day_count = 0
        with open("inputs/day_6_input.txt", "r") as data_file:
            self.raw_data = data_file.readline()
        self.data = self.raw_data.split(",")

        self.school = []

        for fish_age in self.data:
            self.school.append(Fish(int(fish_age)))

    def next_day(self):
        new_fish_count = 0
        for fishy in self.school:
            new_fish = fishy.age_fish()
            if new_fish:
                new_fish_count += 1
        for x in range(new_fish_count):
            self.school.append(Fish(8))
        self.day_count += 1
        print(f"Day {self.day_count} over.")

    def count_fish(self):
        return len(self.school)

    def print_school(self):
        for fishy in self.school:
            print(fishy.timer)


if __name__ == "__main__":
    school_o_fish = School()

    for day in range(256):
        school_o_fish.next_day()
    print(f"There are {school_o_fish.count_fish()} fish")
