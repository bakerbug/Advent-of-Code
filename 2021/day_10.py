class Syntax:
    def __init__(self):
        with open("inputs/day_10_input.txt", "r") as data_file:
            self.input = data_file.readlines()
        self.cleaned_code = []
        self.cleaned = []
        self.error_score = 0

    def clean_code(self):
        stack = []
        for line in self.input:
            is_clean = True
            if len(stack) != 0:
                # print(f"Error! Stack not empty: {self.stack}")
                stack = []
            for cmd in list(line):

                if cmd == "<" or cmd == "(" or cmd == "{" or cmd == "[":
                    stack.append(cmd)
                elif cmd == ")":
                    cmd_open = stack.pop()
                    expected_open = self.find_open(cmd)

                    if cmd_open != expected_open:
                        print(f"Corrupt line: {cmd_open} != {cmd}")
                        self.error_score += 3
                        is_clean = False
                elif cmd == "]":
                    cmd_open = stack.pop()
                    expected_open = self.find_open(cmd)

                    if cmd_open != expected_open:
                        print(f"Corrupt line: {cmd_open} != {cmd}")
                        self.error_score += 57
                        is_clean = False
                elif cmd == "}":
                    cmd_open = stack.pop()
                    expected_open = self.find_open(cmd)

                    if cmd_open != expected_open:
                        print(f"Corrupt line: {cmd_open} != {cmd}")
                        self.error_score += 1197
                        is_clean = False
                elif cmd == ">":
                    cmd_open = stack.pop()
                    expected_open = self.find_open(cmd)

                    if cmd_open != expected_open:
                        print(f"Corrupt line: {cmd_open} != {cmd}")
                        self.error_score += 25137
                        is_clean = False

            if is_clean:
                self.cleaned_code.append(line)

        print(f"Error score: {self.error_score}")

    def complete_code(self):
        for line in self.cleaned_code:
            pass



    def find_open(self, cmd_close):
        if cmd_close == ")":
            return "("
        elif cmd_close == "]":
            return "["
        elif cmd_close == "}":
            return "{"
        elif cmd_close == ">":
            return "<"
        else:
            print(f"WTF is {cmd_close}?")





if __name__ == "__main__":
    syn = Syntax()
    syn.clean_code()
