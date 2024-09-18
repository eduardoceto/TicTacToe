def boardgrid():

    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    return board

def print_board(board):

    print("\n")
    print(board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    print("---------")
    print(board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print("---------")
    print(board[2][0] + " | " + board[2][1] + " | " + board[2][2])
    print("\n")
    


def check_win(board):

    # Check rows
    for row in board:
        if row.count("X") == 3:
            return "X"
        
        if row.count("O") == 3:
            return "O"

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    # Check diagonals      
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    
    # Check for tie
    if " " not in board[0] and " " not in board[1] and " " not in board[2]:
        return "Tie"
    return ""

def choose_first_player():
    player_choice = input("Player 1 choose if you want to be X or O this round: ").strip().upper()
    while player_choice not in ["X", "O"]:
        print("Invalid choice. Please enter X or O")
        player_choice = input().strip().upper()
    return player_choice

def is_space_empty(board, row, col):
    return board[row][col] == " "


def player_move(board, icon, turn):
    if turn==1:
        number=1
    else:
        number=2

    print(f"Your turn player {number}")
    end = input("Press enter E to finish game, if not enter any character: ").strip().upper()
    if end != "E":
        pass
    else:
        return "E"

    while True:
        row = int(input("Enter row (1-3): ").strip())
        row = row - 1
        col = int(input("Enter column (1-3): ").strip())
        col = col - 1
        while row not in range(3) or col not in range(3):
            print("Invalid row or column. Please enter a number between 1 and 3")
            row = int(input("Enter row (1-3): ").strip())
            row = row - 1
            col = int(input("Enter column (1-3): ").strip())
            col = col - 1

        if not is_space_empty(board, row, col):
            print()
            print("That space is taken!")
        else:
            board[row][col] = icon
            break
        

def reset_board(board):
    for row in range(3):
        for col in range(3):
            board[row][col] = " "
            

score1=0
score2=0
round=1
turn=1
board = boardgrid()
current_player = choose_first_player()

while True:
    print(f"This is round {round}.")   
    while True:   
        print_board(board)
        
        if player_move(board, current_player, turn) == "E":
            print("Game Over!")
            break

        winner = check_win(board)

        if winner == "X":
            print_board(board)
            print("X wins! Game over.")
            if turn == 1:
                score1+=1
            else:
                score2+=1
            break
        elif winner == "O":
            print_board(board)
            print("O wins! Game over.")
            if turn == 1:
                score1+=1
            else:
                score2+=1
            break
        elif winner == "Tie":
            print_board(board)
            print("It's a tie! Game over.")
            break
        else:
            pass

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"
        if turn==1:
            turn=2
        else:   
            turn=1

    restart = input("Play again? (Y/N): ")
    if restart.upper() == "N":
        print(f"Player 1 score: {score1}")
        print(f"Player 2 score: {score2}")
        print("/n")
        if score1>score2:
            print("Player 1 wins!")
            print("/n")
        elif score2>score1:
            print("Player 2 wins!")
        else:
            print("It's a tie!")
        print("Bye!")
        break
    else:
        reset_board(board)
        current_player = choose_first_player()
        round+=1