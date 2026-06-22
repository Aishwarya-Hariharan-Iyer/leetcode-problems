class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.board = [[0 for _ in range(n)] for _ in range(n)]

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player
        board = self.board
        n = self.n
        if board[row].count(player) == n:
            return player
        elif [board[i][col] for i in range(self.n)].count(player) == n:
            return player
        elif row == col and [board[i][i] for i in range(self.n)].count(player) == n:
            return player
        elif row + col == n-1 and [board[i][n-1-i] for i in range(self.n)].count(player) == n:
            return player
        else:
            return 0

        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)