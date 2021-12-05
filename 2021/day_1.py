class SonarData:
    def __init__(self):
        data_file = open("inputs/day_1_input.txt", "r")
        self.sonar_data = data_file.readlines()
        data_file.close()

    def find_increases(self):
        init = True
        previous = 0
        count = 0

        for reading in self.sonar_data:
            reading = int(reading)
            if init:
                previous = reading
                init = False
            else:
                if reading > previous:
                    count += 1
                previous = reading

        return count

    def find_windowed_increases(self):
        init = True
        alpha = None
        bravo = None
        charlie = None
        count = 0
        previous = 0

        alpha = int(self.sonar_data[0])
        bravo = int(self.sonar_data[1])
        charlie = int(self.sonar_data[2])
        previous_window = alpha + bravo + charlie

        for reading in self.sonar_data:
            reading = int(reading)
            new_window = bravo + charlie + reading
            if new_window > previous_window:
                count += 1

            previous_window = new_window
            bravo = charlie
            charlie = reading

        return count


if __name__ == "__main__":
    sonar = SonarData()

    print(f"There are {sonar.find_increases()} depth increases.")
    print(f"There are {sonar.find_windowed_increases()} window increases.")
