# game - tic-tac-toe
# rules
import time
import random
def game_rules() -> None:
    """
    transcribes the rulles of Tic Tac Toe
    :return: the game rules
    """
    print(f"""{' ' * 18}---game rules---
1. choose X or O 
2. wait for computer's input
3. if you have 3 in a Row/Column or Diagonal - you have won
4. comuter wins if he has have 3 in a Row/Column or Diagonal
5. its a tie if no one has 3 in a Row/Column or Diagonal
""")


# create a 3 by 3 board that can be updated or resets the board
def draw_board(board: list):
    """
    draws the board on the console
    :param board: bring list of lists- 1-9
    :return: drawn board
    """
    for row in board:
        print('|'.join(row))
        for col in row:
            if row == [' 7 ', ' 8 ', ' 9 ']:
                break
            print('---+---+---')
            break


# a player can pick if he is X or O
def choose_a_symbol() -> str:
    """
    player can choose a symbol
    :return: the symbol the player had chosen
    """
    while True:
        choice = input('enter your choice X or O: ').upper()
        if choice == 'X':
            return ' X '
        elif choice == 'O':
            return ' O '
        print(f'invalid character pleas enter your choice X or O: ')

# the computer's symbol is changed acording to symbol
# choosen by the player.
def switch_player(current: str) -> str:
    """
    a symbol X or O is entered by player and the other one's returned
    :param current: symbol chosen by player
    :return: X or O depending on plaer's symbol
    """
    if current == ' X ':
        return ' O '
    else:
        return ' X '

# player input for board:
# handel's not a number, is between 1-9, space is taken

def ply_turn_to_pic(board: list, symbol: str) -> list:
    """
    gets the board and the symbol. then symbol is placed were chosen by player
    :param board: list of lists with current play
    :param symbol: the symbol chosen by player
    :return: the symbol is place in the board
    """
    row = input(f'enter a column, 1-3: ')
    print()
    col = input(f'enter a row, 1-3: ')
    print()
    while True:
        if row.isdigit() and col.isdigit():
            if board[int(row)-1][int(col)-1] != ' X ' and board[int(row)-1][int(col)-1] != ' O ':
                board[int(row)-1][int(col)-1] = symbol
                return board
            else:
                print(f'invalid moove the space chosen is taken try again: ')
                row = input('enter a column, 1-3 ')
                col = input('enter a row, 1-3 ')
        else:
            row = input('enter a column, 1-3 ')
            col = input('enter a row, 1-3 ')

# computer input for board - should be random
def pc_turn_to_pic(board: list, symbol: str) -> list:
    """
    gets the board and the symbol. then symbol is placed were chosen in random
    :param board: list of lists with current play
    :param symbol: the symbol NOT chosen by player
    :return: the symbol is place in the board
    """
    while True:
        row = random.randint(0,2)
        col = random.randint(0,2)
        while board[row][col] != ' X ' and board[row][col] != ' O ':
            board[row][col] = symbol
            return board
        else:
            row = random.randint(0, 2)
            col = random.randint(0, 2)

def is_tie(board: list) -> bool:
    """
    checks if the board is full if so it's a tie
    :param board: list of lists with current play
    :return: True if the board is full else False
    """
    for row in board:
        for col in row:
            if col not in [' X ', ' O ']:
                return False
    return True


def check_winner(board: list) -> str | None:
    """
    gets the board and decides who won the game. if there are no winners - None return
    :param board: list of lists with current play
    :return: the winner (X or O) or None
    """
    for row in board:
        if row[0] == row[1] == row[2] and row[0] in [' X ', ' O ']:
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] in [' X ', ' O ']:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] in [' X ', ' O ']:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] in [' X ', ' O ']:
        return board[0][2]
    return None

def want_to_play_again():
    play_again = input('Wanna play again? yes or no: ')
    if play_again.isalpha():
        play_again.lower()
        if play_again != 'yes':
            return False
        else:
            print("that's great")
            return True






def play_game() -> None:
    """
    the main brain of the game.
    this function is the loop were the game is being played at
    :return: None
    """

    game_rules()
    board = [
        [' 1 ',' 2 ',' 3 '],
        [' 4 ',' 5 ',' 6 '],
        [' 7 ',' 8 ',' 9 '],
    ]
# choose a symbol for the game X or O and cmp is the other
    players_symbol = choose_a_symbol()
    computer_symbol = switch_player(players_symbol)

    while True:
        # player's turn
        board = ply_turn_to_pic(board, players_symbol)
        time.sleep(1.5)
        draw_board(board)
        # chck if plyer wins
        time.sleep(1.5)
        winner = check_winner(board)
        if winner:
            print(f'Winner is: {winner}')
            break
        # check for ties
        if is_tie(board):
            print('Its a tie!')
            break
        print('---' * 5, "computer's turn", '---' * 5)

        # computer's turn
        board = pc_turn_to_pic(board, computer_symbol)
        time.sleep(1.5)
        draw_board(board)

        # chck if computer wins
        time.sleep(1.5)
        winner = check_winner(board)
        if winner:
            print(f'Winner is:\n {winner} Computer')
            break
        # check for ties
        if is_tie(board):
            print('Its a tie!')
            break
        print('---' * 5, "player's turn", '---' * 5)
    time.sleep(1.5)
    play_again = want_to_play_again()
    if play_again:
        play_game()
    else:
        print('Bye bye')


play_game()
