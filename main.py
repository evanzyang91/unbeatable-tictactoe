import random

def winner(board):
    """
    This function accepts the Tic-Tac-Toe board as a parameter.  
    If there is no winner, the function will return the empty string "".  
    If the user has won, it will return 'X', and if the computer has 
    won it will return 'O'.
    """
    
    # Check rows for winner
    #iterates from 0-2
    for row in range(3):

        #checks if all three col values in the same row are equal
        if (board[row][0] == board[row][1] == board[row][2]) and (board[row][0] != " "):
            #returns the value the squares hold if true
            return board[row][0]

    # Check columns for winner
    #iterates from 0-2
    for col in range(3):

        #checks if all three row values in the same column are equal
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            #returns the value the squares hold if true
            return board[0][col]
    
    # Check diagonal (top-left to bottom-right) for winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    
    # Check diagonal (bottom-left to top-right) for winner
    if board[2][0] == board[1][1] == board[0][2] and board[2][0] != " ":
        return board[2][0]
    
    # No winner: return the empty string
    return ""

def display_board(board):
    """
    This function accepts the Tic-Tac-Toe board as a parameter.  
    It will print the Tic-Tac-Toe board grid (using ASCII characters)
    and show the positions of any X's and O's.  It also displays 
    the column and row numbers on top and beside the board to help
    the user figure out the coordinates of their next move.  
    This function does not return anything.
    """
    
    print("   1   2   3")
    print("1: " + board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    print("  ---+---+---")
    print("2: " + board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print("  ---+---+---")
    print("3: " + board[2][0] + " | " + board[2][1] + " | " + board[2][2])
    print()
    
def make_user_move(board):
    """
    This function accepts the Tic-Tac-Toe board as a parameter.  
    It will ask the user for a row and column.  If the row and 
    column are each within the range of 0 and 2, and that square
    is not already occupied, then it will place an 'X' in that square.
    """
    
    #sets flag to break while loop when valid inputs taken
    valid_move = False

    while not valid_move:

        #tries to take integer inputs
        try:

            #takes user integer inputs
            row = int(input("What row would you like to move to (1-3): "))
            col = int(input("What col would you like to move to (1-3): "))

            #subtracts 1 from user input to get indexes
            row -= 1
            col -= 1

            #validates that inputs are valid indexes
            if (0 <= row <= 2) and (0 <= col <= 2) and (board[row][col] == " "):

                #sets the corresponding square to "X"
                board[row][col] = 'X'

                #shows that move was valid and breaks loop
                valid_move = True

            else:
                print("Sorry, invalid square. Please try again!\n")

        #excepts ValueError that occurs when non-integer is entered
        except ValueError:

            print("Please enter an integer.")
            
            
def make_computer_move(board):
    """
    This function accepts the Tic-Tac-Toe board as a parameter.  
    It will randomly pick row and column values between 0 and 2.  
    If that square is not already occupied it will place an 'O' 
    in that square.  Otherwise, another random row and column 
    will be generated.
    """

    empty = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                empty.append((row, col))

    # shuffle the list of possible moves
    random.shuffle(empty)

    if board[1][1] == " ":
        board[1][1] = "O"
        return
    elif len(empty) == 8:
        corner = random.randint(1, 4)
        if corner == 1:
            board[0][0] = "O"
            return
        elif corner == 2:
            board[0][2] = "O"
            return
        elif corner == 3:
            board[2][0] = "O"
            return
        elif corner == 4:
            board[2][2] = "O"
            return
    
    if len(empty) == 6 and (board[0][0] == board[2][2] or board[2][0] == board[0][2]) and ((board[0][0] != " " and board[2][0] != " ") or (board[0][0] != " " and board[2][0] != " ")):
        side = random.randint(1, 4)
        if side == 1:
            board[1][0] = "O"
            return
        elif side == 2:
            board[1][2] = "O"
            return
        elif side == 3:
            board[0][1] = "O"
            return
        elif side == 4:
            board[2][1] = "O"
            return

    # try to win
    for row, col in empty:
        board[row][col] = "O"
        if winner(board) == "O":
            return
        board[row][col] = " "

    # try to block the user
    for row, col in empty:
        board[row][col] = "X"
        if winner(board) == "X":
            board[row][col] = "O"
            return
        board[row][col] = " "


    # choose a random move
    row, col = random.choice(empty)
    board[row][col] = "O"
    
def main():
    """
    Our Main Game Loop:
    """
    
    free_cells = 9
    users_turn = True
    ttt_board = [ [ " ", " ", " " ], [ " ", " ", " " ], [ " ", " ", " " ] ]

    while not winner(ttt_board) and (free_cells > 0):
        display_board(ttt_board)
        if users_turn:
            make_user_move(ttt_board)
            users_turn = not users_turn
        else:
            make_computer_move(ttt_board)
            users_turn = not users_turn
        free_cells -= 1
        
    display_board(ttt_board)
    if (winner(ttt_board) == 'X'):
        print("Y O U   W O N !")
    elif (winner(ttt_board) == 'O'):
        print("I   W O N !")
    else:
        print("S T A L E M A T E !")
    print("\n*** GAME OVER ***\n")
 
# Start the game!
main()