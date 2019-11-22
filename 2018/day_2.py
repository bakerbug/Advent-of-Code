from typing import Tuple
import itertools


class BoxScanner:
    def __init__(self):
        self.input_data = None
        self.double_count = 0
        self.triple_count = 0
        self.calculated_result = None
        self.pairs = set()

    def display_result(self):
        print(f"Doubles: {self.double_count} Triples: {self.triple_count}")
        self.calculated_result = self.double_count * self.triple_count
        print(f"Calculated result: {self.calculated_result}")

    def read_input(self, file_path):
        try:
            with open(file_path, "r") as input_file:
                self.input_data = input_file.read().splitlines()
        except Exception:
            print(f"Unable to read data from {file_path}")
            exit()

    def scan_list(self):
        for label in self.input_data:
            double, triple = self._scan_label(label)
            if double:
                self.double_count += 1
            if triple:
                self.triple_count += 1

    @staticmethod
    def _scan_label(label: str) -> Tuple:
        found_double = False
        found_triple = False

        for character in label:
            matches = label.count(character)
            if matches == 2:
                found_double = True
            if matches == 3:
                found_triple = True

        return found_double, found_triple

    def find_pairs(self):
        for left, right in itertools.combinations(self.input_data, 2):
            index_id = 0
            misses = 0
            match_list = []
            for letter in left:
                if letter != right[index_id]:
                    misses += 1
                else:
                    match_list.append(letter)
                index_id += 1

            if misses == 1:
                print(f"Found pair {left} and {right}")
                print(f"Match list: {match_list}")
                self.pairs.add((left, right))

    def get_pair_count(self) -> int:
        return len(self.pairs)


if __name__ == "__main__":
    input_file = "./inputs/day_2_input.txt"
    box = BoxScanner()
    box.read_input(input_file)
    box.scan_list()
    box.display_result()
    box.find_pairs()
    print(f"Found {box.get_pair_count()} pairs.")


