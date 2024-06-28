import math

def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)

def winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def full(board):
    return all(cell != ' ' for row in board for cell in row)

def terminal(board):
    return winner(board, 'X') or winner(board, 'O') or full(board)

def evaluate(board):
    if winner(board, 'X'):
        return 1
    elif winner(board, 'O'):
        return -1
    else:
        return 0

def minimax(board, depth, maxplayer, alpha, beta):
    if terminal(board):
        return evaluate(board)
    if maxplayer:
        maxeval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = ' '
                    maxeval = max(maxeval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return maxeval
    else:
        mineval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ' '
                    mineval = min(mineval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return mineval

def getbest(board):
    bestmove = None
    besteval = -math.inf
    alpha = -math.inf
    beta = math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                eval = minimax(board, 0, False, alpha, beta)
                board[i][j] = ' '
                if eval > besteval:
                    besteval = eval
                    bestmove = (i, j)
    return bestmove

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to My Tic-Tac-Toe!")
    print_board(board)
    while not terminal(board):
        while True:
            row = int(input("Enter the row position (0, 1, or 2): "))
            col = int(input("Enter the column position (0, 1, or 2): "))
            if board[row][col] == ' ':
                board[row][col] = 'O'
                break
            else:
                print("Cell is already filled. Please Try another cell.")
        print_board(board)
        if winner(board, 'O'):
            print("Congratulations! You win!")
            break
        elif full(board):
            print("It's a draw!")
            break
        print("AI is thinking...")
        row, col = getbest(board)
        board[row][col] = 'X'
        print_board(board)
        if winner(board, 'X'):
            print("AI wins!")
            break
        elif full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
