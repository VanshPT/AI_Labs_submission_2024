#9580 Vansh Thakkar
#Heuristic_TicTacToe

def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def evaluate(board):
    # Heuristic evaluation function
    if check_winner(board, 'X'):
        return -1  # Player X wins
    elif check_winner(board, 'O'):
        return 1   # Player O wins
    else:
        return 0   # It's a draw

def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, maximizing_player):
    if depth == 0 or check_winner(board, 'X') or check_winner(board, 'O') or is_board_full(board):
        return evaluate(board)

    available_moves = get_available_moves(board)

    if maximizing_player:
        max_eval = float('-inf')
        for move in available_moves:
            i, j = move
            board[i][j] = 'O'
            eval = minimax(board, depth - 1, False)
            board[i][j] = ' '  # Undo the move
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in available_moves:
            i, j = move
            board[i][j] = 'X'
            eval = minimax(board, depth - 1, True)
            board[i][j] = ' '  # Undo the move
            min_eval = min(min_eval, eval)
        return min_eval

def get_best_move(board):
    available_moves = get_available_moves(board)
    best_move = None
    best_eval = float('-inf')

    for move in available_moves:
        i, j = move
        board[i][j] = 'O'
        eval = minimax(board, 2, False)  # You can adjust the depth for a more or less sophisticated AI
        board[i][j] = ' '  # Undo the move

        if eval > best_eval:
            best_eval = eval
            best_move = move

    return best_move

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    game_end = False

    print('Welcome to Tic-Tac-Toe using Heuristic Approach!')

    while not game_end:
        print_board(board)

        # Player's turn
        player_move = tuple(map(int, input('Enter your move (row col): ').split()))
        if board[player_move[0]][player_move[1]] == ' ':
            board[player_move[0]][player_move[1]] = 'X'
        else:
            print('Invalid move. Try again.')
            continue

        # Check if the player wins
        if check_winner(board, 'X'):
            print_board(board)
            print('You win!')
            break

        # Check for a draw
        if is_board_full(board):
            print_board(board)
            print('It\'s a draw!')
            break

        # Computer's turn
        print('Computer\'s turn')
        computer_move = get_best_move(board)
        board[computer_move[0]][computer_move[1]] = 'O'

        # Check if the computer wins
        if check_winner(board, 'O'):
            print_board(board)
            print('Computer wins!')
            break

        # Check for a draw again
        if is_board_full(board):
            print_board(board)
            print('It\'s a draw!')
            break

if __name__ == "__main__":
    main()
    
# OUTPUT:

# Welcome to Tic-Tac-Toe using Heuristic Approach!
     
     
     

# Enter your move (row col): 2 0
# Computer's turn
# O    
     
# X    

# Enter your move (row col): 1 1
# Computer's turn
# O   O
#   X  
# X

# Enter your move (row col): 2 0
# Invalid move. Try again.
# O   O
#   X
# X

# Enter your move (row col): 2 1
# Computer's turn
# O O O
#   X
# X X

# Computer wins!