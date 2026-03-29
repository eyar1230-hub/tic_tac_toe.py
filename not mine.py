#####I did it myself learning with youtube and google####
import pygame
from TIC_TAC_TOE_FOR_ANIMATION import winning_by_row_col_diagonal,path_for_win

pygame.init() # running the pygame

#colors
green = (56,180,97)
red = (255,0,0)
blue = (0,0,255)
black = (0,0,0)
white = (255,255,255)
font = pygame.font.SysFont(None,40)

#create the screen
screen_width = 300
screen_height = 300
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display .set_caption("TIC-TAC-TOE")


def draw_grid():
    color = (192,192,192) #RGB - silver
    grid = (50,50,50)
    screen.fill(color)
    for x in range (1,3):
        pygame.draw.line(screen,grid,(0,x * 100), (screen_width,x * 100))
        pygame.draw.line(screen,grid,(x * 100,0), (x * 100,screen_height))
markers = []
clicked = False
pos = []
win_path = []
line_width = 6
player = 1
winner = None
game_over = False
again_rect = pygame.Rect(screen_width // 2 -80, screen_height // 2 , 160, 50)


for x in range (3):
    row = [0] * 3
    markers.append(row)

def draw_markers():
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen, green, (x_pos * 100 + 15, y_pos * 100 + 15), (x_pos * 100 + 85, y_pos * 100 + 85),line_width)
                pygame.draw.line(screen, green, (x_pos * 100 + 15, y_pos * 100 + 85), (x_pos * 100 + 85, y_pos * 100 + 15),line_width)
            if y == -1:
                pygame.draw.circle(screen,red,(x_pos * 100 + 50, y_pos * 100 + 50), 38,line_width)
            y_pos += 1
        x_pos += 1


def check_winner(current_markers):
    board = [' '] * 9
    for r in range(3):
        for c in range(3):
            cell = current_markers[c][r]
            i = r * 3 + c
            if cell == 1:
                board[i] = 'X'
            elif cell == -1:
                board[i] = 'O'

    ways_to_win = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for path in ways_to_win:
        # בודק אם כל שלוש המשבצות במסלול שוות ל-'X'
        if board[path[0]] == board[path[1]] == board[path[2]] == 'X':
            return 1, True, path
        # בודק אם כל שלוש המשבצות במסלול שוות ל-'O'
        if board[path[0]] == board[path[1]] == board[path[2]] == 'O':
            return 2, True, path
        if ' ' not in board:
            return 0,True, []

    return None, False, []

def draw_winner():
    if winner == 0:
        win_text = "It is a Tie!"
    else:
        win_text = 'Player '+ str(winner) + ' Wins!'
    win_img = font.render(win_text, True, blue)
    pygame.draw.rect(screen,white,(screen_width // 2 -100, screen_height // 2, 60,50))
    screen.blit(win_img, (screen_width // 2 - 100, screen_height // 2 - 50))
    if win_path:
        start = win_path[0]
        end = win_path[2]
        start_x = (start % 3) * 100 + 50
        start_y = (start // 3) * 100 + 50
        end_x = (end % 3) * 100 + 50
        end_y = (end // 3) * 100 + 50

        pygame.draw.line(screen, black, (start_x, start_y), (end_x, end_y), 5)

    text_again = 'play again?'
    img_again = font.render(text_again, True, blue)
    pygame.draw.rect(screen,white,again_rect)
    screen.blit(img_again,(screen_width // 2 -80, screen_height // 2 + 10))

#game loop
running = True
while running:
    draw_grid()
    draw_markers()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if game_over == 0:
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                cell_x = pos[0]
                cell_y = pos[1]
                if markers[cell_x // 100][cell_y // 100] == 0:
                    markers[cell_x // 100][cell_y // 100] = player
                    player *= -1
                    result = check_winner(markers)
                    winner,game_over,win_path = result
    if game_over == True:
        draw_winner()
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == True:
            clicked = False
            pos = pygame.mouse.get_pos()
            if again_rect.collidepoint(pos):
                markers = []
                pos = []
                player = 1
                winner = None
                game_over = False
                for x in range(3):
                    row = [0] * 3
                    markers.append(row)


    pygame.display.update() #update the screen display

pygame.quit()