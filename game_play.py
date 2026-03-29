# game - tic-tac-toe
# rules
import random
def game_rules():
    print(f"""{' ' * 18}---game rules---
1. choose X or O 
2. wait for computer's input
3. if you have 3 in a Row/Column or Diagonal - you have won
4. comuter wins if he has have 3 in a Row/Column or Diagonal
5. its a tie if no one has 3 in a Row/Column or Diagonal
""")


# create a 3 by 3 board that can be updated or resets the board
def draw_board(board):
    for row in board:
        print('|'.join(row))
        for col in row:
            if row == [' 7 ', ' 8 ', ' 9 ']:
                break
            print('---+---+---')
            break
    print('---'*30)

# computer input for board - should be random
def ply_turn_to_pic(board):
    row = input('enter a column, 1-3')
    col = input('enter a row, 1-3')
    while True:
        if row.isdigit() and col.isdigit():

            while board[int(row)-1][int(col)-1] != ' X ' and board[int(row)-1][int(col)-1] != ' O ':
                board[int(row)-1][int(col)-1] = ' X '
                return board
            else:
                row = input('enter a column, 1-3')
                col = input('enter a row, 1-3')


def pc_turn_to_pic(board):
        while True:
            row = random.randint(0,2)
            col = random.randint(0,2)
            while board[row][col] != ' X ' and board[row][col] != ' O ':
                board[row][col] = ' O '
                return board
            else:
                row = random.randint(0, 2)
                col = random.randint(0, 2)


def check_winner(board):
    X_winner == []
    for winner in board:
        if winner == ' X ':
            X_winner.append(' X ')
        pass


# chose placement on the board
#   verify placement == possible
#   place i the rught place

# win\loose\tie
#   loose\win if - row or col or crosses is only X or only O
#   tie if there are no 3 items in a row

# main game loop
#   shows rules
#   asks for you to choose X or O as game pice
#   inputs computer placement
#       cheks if there are no inputs there
#       print board after every placement
#       check for winner
#   input player placement
#       cheks if there are no inputs there
#       print board after every placement
#       check for winner
#   if there is a winner - print winner icon
############################# main code #############################

game_rules()
board = [
    [' 1 ',' 2 ',' 3 '],
    [' 4 ',' 5 ',' 6 '],
    [' 7 ',' 8 ',' 9 '],
]

while True:
    board = ply_turn_to_pic(board)
    draw_board(board)
    if check_winner == True:
        print ('winner is:')
        print(board)
    board = pc_turn_to_pic(board)
    draw_board(board)

