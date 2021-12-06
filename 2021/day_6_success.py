from collections import OrderedDict

if __name__ == "__main__":

    with open("inputs/day_6_input.txt", "r") as file_data:
        data = file_data.readline()
    data = data.rstrip("\n")
    data = data.split(",")

    school = OrderedDict({0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0})
    for fish in data:
        school[int(fish)] += 1

    for day in range(256):
        spawn = school[0]
        school[0] = school[1]
        school[1] = school[2]
        school[2] = school[3]
        school[3] = school[4]
        school[4] = school[5]
        school[5] = school[6]
        school[6] = school[7] + spawn
        school[7] = school[8]
        school[8] = spawn
        print(f"Day {day} complete.")

    total_fish = 0
    for fish in school.values():
        total_fish += fish

    print(f"There are {total_fish} fish.")
