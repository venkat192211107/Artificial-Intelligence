def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve_queens_util(board, col):
    if col >= len(board):
        return True
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_queens_util(board, col + 1):
                return True
            board[i][col] = 0
    return False


def solve_queens():
    board = [[0] * 8 for _ in range(8)]
    if not solve_queens_util(board, 0):
        print("Solution does not exist")
        return False
    print("Solution to the 8-Queens problem:")
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end=" ")
        print()


if __name__ == "__main__":
    solve_queens()