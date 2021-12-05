from copy import deepcopy


class Diagnostic:
    def __init__(self):
        data_file = open("inputs/day_3_input.txt", "r")
        self.data = data_file.readlines()
        self.data_length = len(self.data[0]) - 1
        data_file.close()
        self.gamma = 0
        self.epsilon = 0
        self.oxygen_data = deepcopy(self.data)
        self.co2_data = deepcopy(self.data)

    def find_power(self):
        self.find_gamma()
        self.find_epsilon()
        return self.gamma * self.epsilon

    def find_oxygen(self, place=0):
        if len(self.oxygen_data) == 1:
            return int(self.oxygen_data[0], 2)

        common_bit = self.find_most_common_bit(self.oxygen_data, place)

        if common_bit == "same":
            common_bit = "1"

        self.oxygen_data = self.clean_list(self.oxygen_data, common_bit, place)
        place += 1
        return self.find_oxygen(place)

    def find_co2(self, place=0):
        if len(self.co2_data) == 1:
            return int(self.co2_data[0], 2)

        common_bit = self.find_least_common_bit(self.co2_data, place)

        if common_bit == "same":
            common_bit = "0"

        self.co2_data = self.clean_list(self.co2_data, common_bit, place)
        place += 1
        return self.find_co2(place)

    def find_lifesupport(self):
        oxygen = self.find_oxygen()
        co2 = self.find_co2()
        return oxygen * co2

    def find_gamma(self):
        bit_string = ""
        for place in range(self.data_length):
            bit_string = bit_string + self.find_most_common_bit(self.data, place)

        self.gamma = int(bit_string, 2)
        print(f"Gamma is: {self.gamma}")

    def find_epsilon(self):
        bit_string = ""
        for place in range(self.data_length):
            bit_string = bit_string + self.find_least_common_bit(self.data, place)

        self.epsilon = int(bit_string, 2)
        print(f"Epsilon is: {self.epsilon}")

    def clean_list(self, data_list, keep_value, place):
        index = 0
        kill_list = []
        for reading in data_list:
            if reading[place] != keep_value:
                # print(f"Popping {data_list[index]} with keep of {keep_value} in place {place}")
                kill_list.append(index)
            index += 1

        kill_list.sort(reverse=True)

        for index in kill_list:
            data_list.pop(index)

        return data_list

    def find_most_common_bit(self, data_list, place):
        one = 0
        zero = 0
        for reading in data_list:
            if reading[place] == "1":
                one += 1
            else:
                zero += 1

        if one > zero:
            return "1"
        elif zero > one:
            return "0"
        else:
            return "same"

    def find_least_common_bit(self, data_list, place):
        one = 0
        zero = 0
        for reading in data_list:
            if reading[place] == "1":
                one += 1
            else:
                zero += 1

        if one > zero:
            return "0"
        elif zero > one:
            return "1"
        else:
            return "same"


if __name__ == "__main__":
    diag = Diagnostic()

    print(f"Power consumption is: {diag.find_power()}")
    print(f"Life Support is: {diag.find_lifesupport()}")
