from random import randint
from IPython.display import clear_output

def displayEmpty_board():
    board = ''
    counter = 0

    for i in range(-1, 6):

        if i % 2 == 0:
            board += '|      ' * 4
            board += '\n|  '+str(i+counter+1)+'   |  ' + \
                str(i+counter+2)+'   |   '+str(i+counter+3)+'  |'
            counter += 1 if (i % 2 == 0) else 0
        else:
            board += ' _____ ' * 3

        board += '\n'
    print(board)


def display_board(boardInput):
    clear_output()
    board = ''
    counter = 0

    for i in range(-1, 6):
        if i % 2 == 0:
            board += '|      ' * 4
            board += '\n|  '+str(boardInput[i+counter])+'   |  ' + \
                str(boardInput[i+counter+1])+'   |   ' + \
                str(boardInput[i+counter+2])+'  |'

            counter += 1 if (i % 2 == 0) else 0
        else:
            board += ' _____ ' * 3

        board += '\n'
    print(board)


def player_input():
    player1 = input("Please pick a marker 'X' or 'O': ")
    while(True):
        if player1.upper() == 'X' or player1.upper() == 'O':
            break
        else:
            player1 = input("Please pick a marker 'X' or 'O': ")
    print('Player 1 marker is: ' + player1.upper()
          + '\nPlayer 2 marker is: ' + ('X' if player1.upper() == 'O' else 'O'))
    return player1.upper()


def choose_first():
    # 0 is x and 1 is o
    value = randint(0, 1)
    return 'X' if value == 0 else 'O'


def player_choice(board):
    pChoice = input("Please pick box number: ")

    lOfStrings = [str(x) for x in list(range(1, 10))]

    while pChoice not in lOfStrings or space_check(board, int(pChoice)) == False:
        pChoice = input("Please pick box number: ")
    return int(pChoice)


def place_marker(boardInput, marker, position):
    boardInput[position-1] = marker.upper()
    return boardInput


def win_check(board, mark):
    board = [x.upper() for x in board]
    mark = mark.upper()

    return (board[0] == board[1] == board[2] == mark or
            board[3] == board[4] == board[5] == mark or
            board[6] == board[7] == board[8] == mark or
            board[0] == board[3] == board[6] == mark or
            board[1] == board[4] == board[7] == mark or
            board[2] == board[5] == board[8] == mark or
            board[0] == board[4] == board[8] == mark or
            board[2] == board[4] == board[6] == mark)


def space_check(board, position):
    return board[position-1] == " "


def full_board_check(board):
    return ' ' not in board


def replay():
    replayGame = input('Do you want to replay? Enter Y or N: ')
    while (True):
        if replayGame.upper() == 'Y':
            return True
        elif replayGame.upper() == 'N':
            return False
        else:
            replayGame = input('Do you want to replay? Enter Y or N')


def fullGame():
    print('\n'*100)
    print('Welcome to Tic Tac Toe!')

    while True:
        board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        displayEmpty_board()  # numbered board
        player1Marker = player_input()  # choose x or o

        turn = choose_first()  # who is first x or o
        game_on = True

        while game_on:
            whoPlayer = ''
            if player1Marker == turn:  # Player 1 Turn
                print('Player 1 turn [' + player1Marker + ']')
                whoPlayer = 'Player 1'
            else:  # Player2's turn.
                print('Player 2 turn [' + turn + ']')
                whoPlayer = 'Player 2'

            pChoice = player_choice(board)  # take input from player
            # place the marker who has the current turn
            board = place_marker(board, turn, pChoice)

            display_board(board)

            if win_check(board, turn):
                game_on = False
                print(whoPlayer + '[' + turn + '] has won')
                break

            turn = 'X' if turn == 'O' else 'O'

            if full_board_check(board):
                game_on = False
                print('The game ended with Tie')
                break

        if not replay():
            game_on = True
            break


fullGame()
