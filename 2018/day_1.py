class FrequencyTuner:
    def __init__(self):
        self.BASE_FRQ = 0
        self.input_frq = []
        self.iterations = 0
        self.adjusted_frq = self.BASE_FRQ
        self.unique_frqs = set()
        self.repeat_found = False

    def adjust(self, variance: int):
        self.adjusted_frq = self.adjusted_frq + variance
        if self.adjusted_frq in self.unique_frqs:
            if not self.repeat_found:
                print(f"First duplicate detected: {self.adjusted_frq}")
                self.repeat_found = True
        else:
            self.unique_frqs.add(self.adjusted_frq)

    def read_input(self, file_path):
        try:
            with open(file_path, "r") as input_file:
                self.input_frq = input_file.readlines()
        except Exception:
            print(f"Unable to read data from {file_path}")
            exit()

    def process_input(self):
        while not self.repeat_found:
            if self.iterations == 1:
                print(f"First pass result: {self.adjusted_frq}")
            for adjustment in self.input_frq:
                try:
                    adjustment = int(adjustment)
                    self.adjust(adjustment)
                except ValueError:
                    print(f"Invalid data: {adjustment}")
            self.iterations += 1


if __name__ == "__main__":
    frequency = FrequencyTuner()
    frequency.read_input("frequencies.txt")
    frequency.process_input()
    print(f"Final result: {frequency.adjusted_frq}")
