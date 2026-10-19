import math

def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_terminal_state(board):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8], 
        [0, 4, 8], [2, 4, 6]             
    ]
    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] and board[cond[0]] != ' ':
            return board[cond[0]]
    if ' ' not in board:
        return 'Draw'
    return None

def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_terminal_state(board)
    if winner == 'O':
        return 10 - depth
    elif winner == 'X':
        return depth - 10
    elif winner == 'Draw':
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False, alpha, beta)
                board[i] = ' '
                best_score = max(score, best_score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
        return best_score
    else: 
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True, alpha, beta)
                board[i] = ' '
                best_score = min(score, best_score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
        return best_score

def get_ai_move(board):
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False, -math.inf, math.inf)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

def play_game():
    print("Tic-Tac-Toe: Human ('X') vs AI ('O')")
    print("Indices 0-8 represent rows from left to right, top to bottom.")
    board = [' ' for _ in range(9)]
    print_board(board)
    
    while True:
        try:
            human_move = int(input("Enter your move (0-8): "))
            if board[human_move] != ' ':
                print("Cell occupied!")
                continue
        except (ValueError, IndexError):
            print("Invalid input.")
            continue
            
        board[human_move] = 'X'
        if check_terminal_state(board): break
            
        print("\nAI is making a move...")
        board[get_ai_move(board)] = 'O'
        print_board(board)
        if check_terminal_state(board): break
            
    print_board(board)
    result = check_terminal_state(board)
    if result == 'Draw':
        print("Game Over: It's a Draw!")
    else:
        print(f"Game Over: {result} Wins!")

if __name__ == "__main__":
    play_game()