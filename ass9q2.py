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
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    
    for state in win_states:
        if board[state[0]] == board[state[1]] == board[state[2]] != " ":
            return board[state[0]]
    
    if " " not in board:
        return "Draw"
    
    return None

# Node counter (performance)
node_count = 0

# Alpha-Beta function
def alphabeta(board, is_max, alpha, beta):
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
                score = alphabeta(board, False, alpha, beta)
                board[i] = " "
                best = max(best, score)
                alpha = max(alpha, best)

                # PRUNING
                if beta <= alpha:
                    break
        return best

    else:
        best = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = alphabeta(board, True, alpha, beta)
                board[i] = " "
                best = min(best, score)
                beta = min(beta, best)

                # PRUNING
                if beta <= alpha:
                    break
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
            move_val = alphabeta(board, False, -math.inf, math.inf)
            board[i] = " "

            if move_val > best_val:
                best_val = move_val
                move = i

    print(f"Nodes explored: {node_count}")
    return move

# Game loop
def play_game():
    board = [" "] * 9

    print("TIC-TAC-TOE (Alpha-Beta)")
    print("You = O, AI = X")
    print("Positions 1-9\n")

    while True:
        print_board(board)

        # Player move
        while True:
            try:
                pos = int(input("Enter move (1-9): ")) - 1
                if board[pos] == " ":
                    board[pos] = "O"
                    break
                else:
                    print("Position taken!")
            except:
                print("Invalid input!")

        if check_winner(board):
            break

        print("AI thinking...")
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
        print("Draw!")

# Run
play_game()