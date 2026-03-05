# Tic-Tac-Toe Game using Dictionary

# Create board
theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

board_keys = []

for key in theBoard:
    board_keys.append(key)


# Function to print the board
def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


# Main game function
def game():
    turn = 'X'
    count = 0

    for i in range(9):

        printBoard(theBoard)
        print("It's your turn," + turn + ". Move to which place?")

        move = input()

        if move not in theBoard:
            print("Invalid move! Try again.")
            continue

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.")
            continue

        # Check winner after 5 moves
        if count >= 5:

            # Top row
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print("**** " + turn + " won. ****")
                return

            # Middle row
            if theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print("**** " + turn + " won. ****")
                return

            # Bottom row
            if theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print("**** " + turn + " won. ****")
                return

            # Left column
            if theBoard['7'] == theBoard['4'] == theBoard['1'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print("**** " + turn + " won. ****")
                return

            # Middle column
            if theBoard['8'] == theBoard['5'] == theBoard['2'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print("**** " + turn + " won. ****")
                return

            # Right column
            if theBoard['9'] == theBoard['6'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print("**** " + turn + " won. ****")
                return

            # Diagonal
            if theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print("**** " + turn + " won. ****")
                return

            if theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print("**** " + turn + " won. ****")
                return

        # If board full
        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!")
            return

        # Change player
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'


# Restart option
if __name__ == "__main__":
    game()

    restart = input("Do you want to play again? (y/n): ")

    if restart.lower() == "y":
        for key in board_keys:
            theBoard[key] = " "
        game()
