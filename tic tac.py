board = [" " for _ in range(9)]
def display_board():
    print("-------------")
    for i in range(3):
        print("|", board[i * 3], "|", board[i * 3 + 1], "|", board[i * 3 + 2], "|")
        print("-------------")

def check_winner(player):
    win_conditions = [
        [0, 1, 2],  
        [3, 4, 5],  
        [6, 7, 8], 
        [0, 3, 6], 
        [1, 4, 7],  
        [2, 5, 8],  
        [0, 4, 8],  
        [2, 4, 6]   
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def is_board_full():
    return " " not in board
def make_move(position, player):
    if board[position] == " ":
        board[position] = player
        return True
    return False
def play_game():
    current_player = "X"
    while True:
        display_board()
        try:
            position = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if position < 0 or position > 8:
                print("Invalid move. Please enter a number between 1 and 9.")
                continue
            if not make_move(position, current_player):
                print("That spot is already taken. Try another.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue
        if check_winner(current_player):
            display_board()
            print(f"Player {current_player} wins!")
            break
        if is_board_full():
            display_board()
            print("It's a tie!")
            break
        current_player = "O" if current_player == "X" else "X"
play_game()
