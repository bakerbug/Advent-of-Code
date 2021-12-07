from collections import Counter


class Crabs:
    def __init__(self):
        with open("inputs/day_7_inputs.txt", "r") as data_file:
            raw_data = data_file.readline()
        raw_data = raw_data.rstrip("\n")
        raw_data = raw_data.split(",")
        self.data = []
        for item in raw_data:
            self.data.append(int(item))

        self.positions = Counter(self.data)
        self.position_costs = []

    def find_fuel_cost(self, position):
        total_cost = 0
        for crab in self.data:
            total_cost += abs(position - crab)
        return total_cost

    def find_advanced_fuel_cost(self, position):
        total_cost = 0
        for crab in self.data:
            basic_cost = abs(position - crab)
            penalty = 0
            total_cost += basic_cost
            for this_step in range(basic_cost):
                total_cost += penalty
                penalty += 1
        return total_cost

    def find_costs(self):
        for best_guess in range(max(self.data)):  # Using Counter ultimately was a big mistake.
            this_cost = self.find_advanced_fuel_cost(best_guess)
            self.position_costs.append(this_cost)
            print(f"Cost for position {best_guess} is {this_cost}")
        # self.position_costs.append(self.find_advanced_fuel_cost(5))

    def find_lowest_cost(self):
        self.find_costs()
        best_cost = min(self.position_costs)
        print(f"Lowest fuel cost is {best_cost}")


if __name__ == "__main__":
    swarm = Crabs()
    swarm.find_lowest_cost()
