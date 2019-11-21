class FrequencyTuner:
    def __init__(self):
        self.BASE_FRQ = 0
        self.adjusted_frq = self.BASE_FRQ

    def adjust(self, variance: int) -> int:
        self.adjusted_frq = self.adjusted_frq + variance


if __name__ == "__main__":
    complete = False
    frequency = FrequencyTuner()

    while not complete:
        try:
            new_variance = int(input())
            frequency.adjust(new_variance)
        except ValueError:
            print(f'Adjusted frequency is {frequency.adjusted_frq}.')
            complete = True
