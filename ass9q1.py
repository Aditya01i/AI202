import math

# Print board
def print_board(board):
    print("\n")
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("--+---+--")
    print("\n")

# Check winner
def check_winner(board):
    win_states = [
        [0,1,2],[3,4,5],[6,7,8],  # rows
        [0,3,6],[1,4,7],[2,5,8],  # cols
        [0,4,8],[2,4,6]           # diagonals
    ]
    
    for state in win_states:
        if board[state[0]] == board[state[1]] == board[state[2]] != " ":
            return board[state[0]]
    
    if " " not in board:
        return "Draw"
    
    return None

# Count nodes (performance evaluation)
node_count = 0

# Minimax algorithm
def minimax(board, depth, is_max):
    global node_count
    node_count += 1

    result = check_winner(board)

    if result == "X":
        return 1
    elif result == "O":
        return -1
    elif result == "Draw":
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best = max(best, score)
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best = min(best, score)
        return best

# Find best move
def best_move(board):
    global node_count
    node_count = 0

    best_val = -math.inf
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            move_val = minimax(board, 0, False)
            board[i] = " "

            if move_val > best_val:
                move = i
                best_val = move_val

    print(f"AI evaluated {node_count} nodes.")
    return move

# Main game loop
def play_game():
    board = [" "] * 9

    print("TIC-TAC-TOE")
    print("You are O, AI is X")
    print("Positions are 1-9\n")

    while True:
        print_board(board)

        # Player move
        while True:
            try:
                pos = int(input("Enter your move (1-9): ")) - 1
                if board[pos] == " ":
                    board[pos] = "O"
                    break
                else:
                    print("Position already taken!")
            except:
                print("Invalid input!")

        if check_winner(board):
            break

        # AI move
        print("AI is thinking...")
        move = best_move(board)
        board[move] = "X"

        if check_winner(board):
            break

    print_board(board)
    result = check_winner(board)

    if result == "X":
        print("AI Wins!")
    elif result == "O":
        print("You Win!")
    else:
        print("It's a Draw!")

# Run game
play_game()