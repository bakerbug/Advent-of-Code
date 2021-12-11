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
                    expected_open = self.find_opposite(cmd)

                    if cmd_open != expected_open:
                        print(f"Corrupt line: {cmd_open} != {cmd}")
                        self.error_score += 3
                        is_clean = False
                elif cmd == "]":
                    cmd_open = stack.pop()
                    expected_open = self.find_opposite(cmd)

                    if cmd_open != expected_open:
                        print(f"Corrupt line: {cmd_open} != {cmd}")
                        self.error_score += 57
                        is_clean = False
                elif cmd == "}":
                    cmd_open = stack.pop()
                    expected_open = self.find_opposite(cmd)

                    if cmd_open != expected_open:
                        print(f"Corrupt line: {cmd_open} != {cmd}")
                        self.error_score += 1197
                        is_clean = False
                elif cmd == ">":
                    cmd_open = stack.pop()
                    expected_open = self.find_opposite(cmd)

                    if cmd_open != expected_open:
                        print(f"Corrupt line: {cmd_open} != {cmd}")
                        self.error_score += 25137
                        is_clean = False

            if is_clean:
                self.cleaned_code.append(line)

        print(f"Error score: {self.error_score}\n")

    def complete_code(self):
        score_list = []
        for line in self.cleaned_code:
            stack = []
            line_score = 0
            for cmd in list(line):
                if cmd == "<" or cmd == "(" or cmd == "{" or cmd == "[":
                    stack.append(cmd)
                elif cmd == ">" or cmd == ")" or cmd == "}" or cmd == "]":
                    stack.pop()

            # print(f"stack: {stack}")

            for index in range(len(stack)):
                cmd = stack.pop()
                close = self.find_opposite(cmd)
                line_score = (line_score * 5) + self.character_score(close)

            # print(f"Line score: {line_score}")
            score_list.append(line_score)
        score_list.sort()
        # print(f"Score List: {score_list}")
        score_len = len(score_list)
        mid_point = round(score_len / 2)

        print(f"Final Score: {score_list[mid_point]}")

    def character_score(self, char):
        if char == ")":
            return 1
        elif char == "]":
            return 2
        elif char == "}":
            return 3
        elif char == ">":
            return 4

    def find_opposite(self, command):
        if command == ")":
            return "("
        elif command == "]":
            return "["
        elif command == "}":
            return "{"
        elif command == ">":
            return "<"
        elif command == "(":
            return ")"
        elif command == "[":
            return "]"
        elif command == "{":
            return "}"
        elif command == "<":
            return ">"
        else:
            print(f"WTF is {command}?")


if __name__ == "__main__":
    syn = Syntax()
    syn.clean_code()
    syn.complete_code()
