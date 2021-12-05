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
                    count +=1
                previous = reading

        return count


if __name__ == "__main__":
    sonar = SonarData()

    print(f"There are {sonar.find_increases()} depth increases.")

