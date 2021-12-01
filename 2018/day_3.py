import itertools

class ClaimRecord:
    def __init__(self, data: str):
        words = data.split()
        self.claim_id = str(words[0][1:])
        self.left_offset, self.top_offset = words[2].split(',')
        self.top_offset = self.top_offset[:-1]
        self.width, self.height = words[3].split('x')

        self.left_offset = int(self.left_offset)
        self.top_offset = int(self.top_offset)
        self.height = int(self.height)
        self.width = int(self.width)

        self.tl = {"x": self.left_offset, "y": self.top_offset}
        self.tr = {"x": self.left_offset + self.width, "y": self.top_offset}
        self.bl = {"x": self.left_offset, "y": self.top_offset + self.height}
        self.br = {"x": self.left_offset + self.width, "y": self.top_offset + self.height}
        self.corners = [self.tl, self.tr, self.bl, self.br]

        self.overlap = False

    def get_area(self) -> int:
        return self.width * self.height

class PatchMap:
    def __init__(self):
        self.claim_list = []
        self.total_overlap: int


    def read_input(self, file_path):
        try:
            with open(file_path, "r") as input_file:
                input_data = input_file.read().splitlines()
        except Exception:
            print(f"Unable to read data from {file_path}")
            exit()

        for entry in input_data:
            self.claim_list.append(ClaimRecord(entry))

    def compare_patches(self):
        for alpha, bravo in itertools.combinations(self.claim_list, 2):
            overlap = False
            for alpha_corner, bravo_corner in alpha.corners, bravo.corners:
                if alpha.corner['x'] <= bravo.tl['x'] and alpha.tr['x'] >= bravo

    def print_records(self):
        for record in self.claim_list:
            print(f"ID: {record.claim_id}")
            print(f"Left: {record.left_offset}")
            print(f"Top: {record.top_offset}")
            print(f"Width: {record.width}")
            print(f"Height: {record.height}")

    def print_corners(self):
        for record in self.claim_list:
            print(f"TL: {record.tl['x']}, {record.tl['y']}")
            print(f"TR: {record.tr['x']}, {record.tr['y']}")
            print(f"BL: {record.bl['x']}, {record.bl['y']}")
            print(f"BR: {record.br['x']}, {record.br['y']}")


if __name__ == "__main__":
    input_file = "./inputs/day_3_input.txt"
    coat = PatchMap()
    coat.read_input(input_file)
    coat.print_corners()
