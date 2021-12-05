class Diagnostic:
    def __init__(self):
        data_file = open("inputs/day_3_input.txt", "r")
        self.data = data_file.readlines()
        data_file.close()
        self.gamma = 0
        self.epsilon = 0

    def find_power(self):
        self.find_gamma()
        self.find_epsilon()
        return self.gamma * self.epsilon

    def find_gamma(self):
        bit_string = ""
        for place in range(len(self.data[0]) - 1):
            bit_string = bit_string + self.find_most_common_bit(place)

        self.gamma = int(bit_string, 2)
        print(f"Gamma is: {self.gamma}")

    def find_epsilon(self):
        bit_string = ""
        for place in range(len(self.data[0]) - 1):
            bit_string = bit_string + self.find_least_common_bit(place)

        self.epsilon = int(bit_string, 2)
        print(f"Epsilon is: {self.epsilon}")

    def find_most_common_bit(self, place):
        one = 0
        zero = 0
        for reading in self.data:
            if reading[place] == "1":
                one += 1
            else:
                zero += 1

        if one > zero:
            return "1"
        else:
            return "0"

    def find_least_common_bit(self, place):
        one = 0
        zero = 0
        for reading in self.data:
            if reading[place] == "1":
                one += 1
            else:
                zero += 1

        if one > zero:
            return "0"
        else:
            return "1"


if __name__ == "__main__":
    diag = Diagnostic()

    print(f"Power consumption is: {diag.find_power()}")
