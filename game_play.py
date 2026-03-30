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
    print('---'*5, 'next turn', '---'*5)

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

    for row in board:
        if row[0] == row[1] == row[2] and row[0] in [' X ', ' O ']:
            return row[0]  # יחזיר ' X ' או ' O '
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] in [' X ', ' O ']:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] in [' X ', ' O ']:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] in [' X ', ' O ']:
        return board[0][2]
    return None

def is_tie(board):
    for row in board:
        for col in row:
            if col not in [' X ', ' O ']:
                return False
    return True





game_rules()
board = [
    [' 1 ',' 2 ',' 3 '],
    [' 4 ',' 5 ',' 6 '],
    [' 7 ',' 8 ',' 9 '],
]

while True:
    board = ply_turn_to_pic(board)
    draw_board(board)

    winner = check_winner(board)
    if winner:
        print (f'winner is: {winner}\n{board}')
        break
    if is_tie(board):
        print (f'its a tie {board}')
        break

    board = pc_turn_to_pic(board)
    draw_board(board)

    winer = check_winner(board)
    if check_winner == True:
        print (f'winner is: you \n{draw_board(board)}')
        break
    if is_tie(board):
        print (f'winner is: computer\n{draw_board(board)}')
        break

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
# def check_winner(board):
#     winner = None
#     for row in board[0]:
#         if row == [' X ', ' X ', ' X ']:
#             winner = 'congratulation you won the match!!!'
#             return winner
#         elif row == [' O ', ' O ', ' O ']:
#             winner = 'congratulation you won the match!!!'
#             return winner
#     else:
#         return board