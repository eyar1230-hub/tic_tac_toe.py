import pygame
import sys
import random
import os

# ──────────────────────────────────────────────
#  Pure logic – copied as-is from your original
#  game file (no changes made).
# ──────────────────────────────────────────────
def switch_player(current: str) -> str:
    if current == ' X ':
        return ' O '
    return ' X '

def pc_turn_to_pic(board: list, symbol: str) -> list:
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] not in [' X ', ' O ']:
            board[row][col] = symbol
            return board

def is_tie(board: list) -> bool:
    for row in board:
        for col in row:
            if col not in [' X ', ' O ']:
                return False
    return True

def check_winner(board: list):
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

# ──────────────────────────────────────────────
#  Pygame UI
# ──────────────────────────────────────────────
pygame.init()

# ── Window ──────────────────────────────────
WIDTH, HEIGHT = 540, 680
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# ── Colours ──────────────────────────────────
BG          = (15,  15,  25)
GRID_COL    = (200, 200, 220)
BTN_NORM    = (40,  40,  60)
BTN_HOVER   = (70,  70, 100)
BTN_EXIT    = (120,  30,  30)
BTN_EXIT_H  = (180,  50,  50)
BTN_PLAY    = (30,  90,  50)
BTN_PLAY_H  = (50, 140,  80)
WHITE       = (255, 255, 255)
GOLD        = (255, 215,   0)
RED_SOFT    = (255, 100, 100)
SHADOW      = (0,   0,   0, 120)

# ── Fonts ────────────────────────────────────
FONT_BIG   = pygame.font.SysFont("Arial", 44, bold=True)
FONT_MED   = pygame.font.SysFont("Arial", 26, bold=True)
FONT_SMALL = pygame.font.SysFont("Arial", 20)

# ── Board geometry ───────────────────────────
CELL     = 160          # cell size
GRID_X   = (WIDTH  - CELL * 3) // 2   # 30
GRID_Y   = 130
IMG_SIZE = 110          # symbol image size inside cell
IMG_OFF  = (CELL - IMG_SIZE) // 2     # centring offset

# ── Load symbol images ───────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def _load(name):
    path = os.path.join(BASE_DIR, name)
    img  = pygame.image.load(path).convert_alpha()
    return pygame.transform.smoothscale(img, (IMG_SIZE, IMG_SIZE))

x_img = _load("x_symbol.png")
o_img = _load("o_symbol.png")

# ──────────────────────────────────────────────
#  Helper – draw a rounded button
# ──────────────────────────────────────────────
def draw_button(rect, text, normal_col, hover_col, font=FONT_MED):
    mx, my = pygame.mouse.get_pos()
    hovered = rect.collidepoint(mx, my)
    colour  = hover_col if hovered else normal_col
    pygame.draw.rect(screen, colour, rect, border_radius=12)
    pygame.draw.rect(screen, GRID_COL, rect, 2, border_radius=12)
    lbl = font.render(text, True, WHITE)
    screen.blit(lbl, lbl.get_rect(center=rect.center))
    return hovered

# ──────────────────────────────────────────────
#  Helper – draw the 3×3 grid
# ──────────────────────────────────────────────
def draw_grid():
    for i in range(1, 3):
        # vertical lines
        x = GRID_X + i * CELL
        pygame.draw.line(screen, GRID_COL, (x, GRID_Y), (x, GRID_Y + CELL * 3), 3)
        # horizontal lines
        y = GRID_Y + i * CELL
        pygame.draw.line(screen, GRID_COL, (GRID_X, y), (GRID_X + CELL * 3, y), 3)

# ──────────────────────────────────────────────
#  Helper – draw symbols on the board
# ──────────────────────────────────────────────
def draw_pieces(board):
    for r in range(3):
        for c in range(3):
            cell_x = GRID_X + c * CELL + IMG_OFF
            cell_y = GRID_Y + r * CELL + IMG_OFF
            if board[r][c] == ' X ':
                screen.blit(x_img, (cell_x, cell_y))
            elif board[r][c] == ' O ':
                screen.blit(o_img, (cell_x, cell_y))

# ──────────────────────────────────────────────
#  Screen: choose symbol (X or O)
# ──────────────────────────────────────────────
def screen_choose_symbol():
    btn_x     = pygame.Rect(100, 320, 130, 130)
    btn_o     = pygame.Rect(310, 320, 130, 130)
    btn_quit  = pygame.Rect(WIDTH // 2 - 80, 490, 160, 48)

    clock = pygame.time.Clock()
    while True:
        screen.fill(BG)
        title = FONT_BIG.render("Tic  Tac  Toe", True, GOLD)
        screen.blit(title, title.get_rect(center=(WIDTH // 2, 80)))
        sub   = FONT_MED.render("Choose your symbol", True, WHITE)
        screen.blit(sub, sub.get_rect(center=(WIDTH // 2, 150)))

        # X button
        mx, my = pygame.mouse.get_pos()
        col_x = BTN_HOVER if btn_x.collidepoint(mx, my) else BTN_NORM
        pygame.draw.rect(screen, col_x, btn_x, border_radius=14)
        pygame.draw.rect(screen, GRID_COL, btn_x, 2, border_radius=14)
        xi = pygame.transform.smoothscale(x_img, (90, 90))
        screen.blit(xi, xi.get_rect(center=btn_x.center))

        # O button
        col_o = BTN_HOVER if btn_o.collidepoint(mx, my) else BTN_NORM
        pygame.draw.rect(screen, col_o, btn_o, border_radius=14)
        pygame.draw.rect(screen, GRID_COL, btn_o, 2, border_radius=14)
        oi = pygame.transform.smoothscale(o_img, (90, 90))
        screen.blit(oi, oi.get_rect(center=btn_o.center))

        draw_button(btn_quit, "Quit", BTN_EXIT, BTN_EXIT_H)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if btn_x.collidepoint(event.pos):
                    return ' X '
                if btn_o.collidepoint(event.pos):
                    return ' O '
                if btn_quit.collidepoint(event.pos):
                    pygame.quit(); sys.exit()
        clock.tick(60)

# ──────────────────────────────────────────────
#  Screen: winner / tie result
# ──────────────────────────────────────────────
def screen_result(outcome: str, winner_sym: str | None):
    """
    outcome   : 'win' | 'lose' | 'tie'
    winner_sym: ' X ' or ' O ' (None for tie)
    Returns   : 'again' | 'menu' | 'quit'
    """
    btn_again = pygame.Rect(WIDTH // 2 - 170, 430, 150, 52)
    btn_menu  = pygame.Rect(WIDTH // 2 +  20, 430, 150, 52)
    btn_quit  = pygame.Rect(WIDTH // 2 -  75, 510, 150, 52)

    # Animated pulse for the symbol
    pulse     = 0
    clock     = pygame.time.Clock()

    # Colours & text per outcome
    if outcome == 'win':
        headline  = "You Win!"
        sub_text  = "Great job!"
        h_colour  = GOLD
        bg_tint   = (20, 50, 20)
    elif outcome == 'lose':
        headline  = "CPU Wins!"
        sub_text  = "Better luck next time…"
        h_colour  = RED_SOFT
        bg_tint   = (50, 10, 10)
    else:
        headline  = "It's a Tie!"
        sub_text  = "So close!"
        h_colour  = (140, 200, 255)
        bg_tint   = (20, 20, 50)

    while True:
        pulse += 0.05
        screen.fill(bg_tint)

        # ── Decorative faded grid lines ─────────
        for i in range(1, 3):
            pygame.draw.line(screen, (50, 50, 70),
                             (GRID_X + i * CELL, 0),
                             (GRID_X + i * CELL, HEIGHT), 1)
            pygame.draw.line(screen, (50, 50, 70),
                             (0, GRID_Y + i * CELL),
                             (WIDTH, GRID_Y + i * CELL), 1)

        # ── Headline ────────────────────────────
        h = FONT_BIG.render(headline, True, h_colour)
        screen.blit(h, h.get_rect(center=(WIDTH // 2, 130)))

        sub = FONT_MED.render(sub_text, True, WHITE)
        screen.blit(sub, sub.get_rect(center=(WIDTH // 2, 190)))

        # ── Pulsing winner symbol ────────────────
        if winner_sym is not None:
            scale = int(160 + 18 * abs(__import__('math').sin(pulse)))
            img   = x_img if winner_sym == ' X ' else o_img
            big   = pygame.transform.smoothscale(img, (scale, scale))
            screen.blit(big, big.get_rect(center=(WIDTH // 2, 310)))
        else:
            # Tie: show both symbols side by side
            xi = pygame.transform.smoothscale(x_img, (120, 120))
            oi = pygame.transform.smoothscale(o_img, (120, 120))
            screen.blit(xi, xi.get_rect(center=(WIDTH // 2 - 80, 310)))
            screen.blit(oi, oi.get_rect(center=(WIDTH // 2 + 80, 310)))

        # ── Buttons ─────────────────────────────
        draw_button(btn_again, "Play Again", BTN_PLAY,  BTN_PLAY_H,  FONT_SMALL)
        draw_button(btn_menu,  "Menu",       BTN_NORM,  BTN_HOVER,   FONT_SMALL)
        draw_button(btn_quit,  "Quit",       BTN_EXIT,  BTN_EXIT_H,  FONT_SMALL)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if btn_again.collidepoint(event.pos):
                    return 'again'
                if btn_menu.collidepoint(event.pos):
                    return 'menu'
                if btn_quit.collidepoint(event.pos):
                    pygame.quit(); sys.exit()

        clock.tick(60)


# ──────────────────────────────────────────────
#  Screen: main game play
# ──────────────────────────────────────────────
def screen_play(player_sym):
    comp_sym = switch_player(player_sym)

    board = [
        [' 1 ', ' 2 ', ' 3 '],
        [' 4 ', ' 5 ', ' 6 '],
        [' 7 ', ' 8 ', ' 9 '],
    ]

    # UI buttons (bottom bar)
    btn_quit   = pygame.Rect(30,  622, 140, 42)
    btn_again  = pygame.Rect(200, 622, 140, 42)
    btn_menu   = pygame.Rect(370, 622, 140, 42)

    status_msg = "Your turn"
    pc_pending = False
    pc_timer   = 0
    PC_DELAY   = 700       # ms

    clock = pygame.time.Clock()

    def fresh_board():
        return [
            [' 1 ', ' 2 ', ' 3 '],
            [' 4 ', ' 5 ', ' 6 '],
            [' 7 ', ' 8 ', ' 9 '],
        ]

    def handle_end(winner_sym, is_player_winner):
        """Open the result screen; return 'again'|'menu'."""
        if winner_sym is None:
            outcome = 'tie'
        elif is_player_winner:
            outcome = 'win'
        else:
            outcome = 'lose'
        return screen_result(outcome, winner_sym)

    while True:
        now = pygame.time.get_ticks()
        screen.fill(BG)

        # ── Title bar ──────────────────────────
        title = FONT_MED.render("Tic  Tac  Toe", True, GOLD)
        screen.blit(title, title.get_rect(center=(WIDTH // 2, 30)))

        # Player symbol indicator
        sym_label = FONT_SMALL.render("You:", True, WHITE)
        screen.blit(sym_label, (GRID_X, 62))
        pi = pygame.transform.smoothscale(
            x_img if player_sym == ' X ' else o_img, (34, 34))
        screen.blit(pi, (GRID_X + 46, 57))

        comp_label = FONT_SMALL.render("CPU:", True, WHITE)
        screen.blit(comp_label, (GRID_X + CELL * 3 - 100, 62))
        ci = pygame.transform.smoothscale(
            x_img if comp_sym == ' X ' else o_img, (34, 34))
        screen.blit(ci, (GRID_X + CELL * 3 - 55, 57))

        # ── Grid & pieces ──────────────────────
        draw_grid()
        draw_pieces(board)

        # ── Status message ─────────────────────
        msg = FONT_SMALL.render(status_msg, True, GRID_COL)
        screen.blit(msg, msg.get_rect(center=(WIDTH // 2, GRID_Y + CELL * 3 + 30)))

        # ── Bottom buttons ─────────────────────
        draw_button(btn_quit,  "Quit",       BTN_EXIT,  BTN_EXIT_H,  FONT_SMALL)
        draw_button(btn_again, "Play again", BTN_PLAY,  BTN_PLAY_H,  FONT_SMALL)
        draw_button(btn_menu,  "Menu",       BTN_NORM,  BTN_HOVER,   FONT_SMALL)

        pygame.display.flip()

        # ── Schedule computer move ─────────────
        if pc_pending:
            if now - pc_timer >= PC_DELAY:
                board = pc_turn_to_pic(board, comp_sym)
                pc_pending = False
                winner = check_winner(board)
                if winner:
                    action = handle_end(winner, winner == player_sym)
                    if action == 'again':
                        board = fresh_board(); status_msg = "Your turn"
                    else:
                        return action
                elif is_tie(board):
                    action = handle_end(None, False)
                    if action == 'again':
                        board = fresh_board(); status_msg = "Your turn"
                    else:
                        return action
                else:
                    status_msg = "Your turn"

        # ── Events ────────────────────────────
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = event.pos

                # Bottom buttons
                if btn_quit.collidepoint(mx, my):
                    pygame.quit(); sys.exit()
                if btn_again.collidepoint(mx, my):
                    board = fresh_board(); status_msg = "Your turn"; pc_pending = False
                    continue
                if btn_menu.collidepoint(mx, my):
                    return "menu"

                # Board click → player's move
                if pc_pending:
                    continue
                bx = mx - GRID_X
                by = my - GRID_Y
                if 0 <= bx < CELL * 3 and 0 <= by < CELL * 3:
                    col = bx // CELL
                    row = by // CELL
                    if board[row][col] not in [' X ', ' O ']:
                        board[row][col] = player_sym
                        winner = check_winner(board)
                        if winner:
                            action = handle_end(winner, winner == player_sym)
                            if action == 'again':
                                board = fresh_board(); status_msg = "Your turn"
                            else:
                                return action
                        elif is_tie(board):
                            action = handle_end(None, False)
                            if action == 'again':
                                board = fresh_board(); status_msg = "Your turn"
                            else:
                                return action
                        else:
                            status_msg = "CPU is thinking…"
                            pc_pending = True
                            pc_timer   = pygame.time.get_ticks()

        clock.tick(60)

# ──────────────────────────────────────────────
#  Entry point
# ──────────────────────────────────────────────
def main():
    player_sym = screen_choose_symbol()
    while True:
        result = screen_play(player_sym)
        if result == "menu":
            player_sym = screen_choose_symbol()
        else:
            break

main()
