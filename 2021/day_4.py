class Bingo:
    def __init__(self):
        self.move_data = []
        data_file = open("inputs/day_4_input.txt", "r")
        self.move_raw_data = data_file.readline()
        self.move_raw_data = self.move_raw_data.split(",")
        for move in self.move_raw_data:
            self.move_data.append(int(move))
        self.board_raw_data = data_file.readlines()
        data_file.close()
        self.boards = []
        self.results = []
        self.winning_boards = []
        self.parse_board_data()

    def check_rows(self, board):
        row_id = 0
        for row in board:
            winner = True
            number_id = 0
            for number in row:
                if number is not True:
                    winner = False
            if winner:
                return True
        return False

    def check_columns(self, board):
        column_width = len(self.results[0][0])
        for column_id in range(column_width):
            winner = True
            for row in board:
                if row[column_id] is not True:
                    winner = False
            if winner:
                return True
        return False

    def find_winning_board(self):
        board_id = 0
        winners = []
        for board in self.results:
            if board_id in self.winning_boards:
                pass
            else:
                if self.check_rows(board) or self.check_columns(board):
                    self.winning_boards.append(board_id)
                    winners.append(board_id)
            board_id += 1
        return winners

    def parse_board_data(self):
        board = []
        result = []
        row_count = 0
        for item in self.board_raw_data:
            if item == "\n":
                row_count = 0
                board = []
                result = []
            else:
                row_data = item.rstrip("\n")
                row_data = row_data.split()
                new_row = []
                for item in row_data:
                    new_row.append(int(item))
                board.append(new_row)
                result.append([False, False, False, False, False])
                row_count += 1

            if row_count == 4:
                self.boards.append(board)
                self.results.append(result)

    def add_move(self, move):
        board_id = 0
        for board in self.boards:
            if board_id in self.winning_boards:
                pass
            else:
                row_id = 0
                for row in board:
                    number_id = 0
                    for number in row:
                        if int(move) == int(number):
                            # print(f"Setting Board {board_id}, Row {row_id}, Number {number_id}")
                            self.results[board_id][row_id][number_id] = True
                        number_id += 1
                    row_id += 1
            board_id += 1

    def find_sum_of_board(self, board_id):
        result = 0
        row_id = 0
        for row in self.results[board_id]:
            number_id = 0
            for number in row:
                if number is not True:
                    result += int(self.boards[board_id][row_id][number_id])
                number_id += 1
            row_id += 1

        return result

    def play_games(self):
        for move in self.move_data:
            if len(self.winning_boards) == len(self.boards):
                print("All boards have won!")
                exit()
            self.add_move(move)
            winning_boards = self.find_winning_board()

            for winning_board in winning_boards:
                if winning_board >= 0:
                    board_sum = self.find_sum_of_board(winning_board)
                    print(f"The winning board is {winning_board}")
                    print(f"The winning board sum is {board_sum}")
                    print(f"The last move was {move}")
                    print(f"The final score is {board_sum * int(move)}")
                    print(f"The winners list is: {self.winning_boards}\n")

                    for row in self.results[winning_board]:
                        print(row)
                    print("\n")


if __name__ == "__main__":
    game = Bingo()
    game.play_games()
