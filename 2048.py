import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH = 500
HEIGHT = 600
GRID_SIZE = 4
CELL_SIZE = 100
MARGIN = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")

# Clock
clock = pygame.time.Clock()

# Colors
BACKGROUND = (187, 173, 160)
EMPTY_CELL = (205, 193, 180)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Tile colors
TILE_COLORS = {
    0: (205, 193, 180),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46)
}

# Font
font = pygame.font.SysFont("Arial", 40, bold=True)
small_font = pygame.font.SysFont("Arial", 28)

# Game board
board = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]

# Score
score = 0



def add_new_tile():
    empty_cells = []

    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if board[row][col] == 0:
                empty_cells.append((row, col))

    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = 2 if random.random() < 0.9 else 4



def draw_board():
    screen.fill(BACKGROUND)

    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            value = board[row][col]

            x = col * (CELL_SIZE + MARGIN) + MARGIN
            y = row * (CELL_SIZE + MARGIN) + 100

            color = TILE_COLORS.get(value, (60, 58, 50))

            pygame.draw.rect(
                screen,
                color,
                (x, y, CELL_SIZE, CELL_SIZE),
                border_radius=8
            )

            if value != 0:
                text_color = BLACK if value <= 4 else WHITE
                text = font.render(str(value), True, text_color)
                text_rect = text.get_rect(center=(x + CELL_SIZE // 2, y + CELL_SIZE // 2))
                screen.blit(text, text_rect)

    # Draw score
    score_text = small_font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (20, 30))



def compress(row):
    new_row = [num for num in row if num != 0]
    new_row += [0] * (GRID_SIZE - len(new_row))
    return new_row



def merge(row):
    global score

    for i in range(GRID_SIZE - 1):
        if row[i] == row[i + 1] and row[i] != 0:
            row[i] *= 2
            score += row[i]
            row[i + 1] = 0

    return row



def move_left():
    changed = False

    for row in range(GRID_SIZE):
        original = board[row][:]

        compressed = compress(board[row])
        merged = merge(compressed)
        final = compress(merged)

        board[row] = final

        if original != final:
            changed = True

    return changed



def reverse():
    for row in range(GRID_SIZE):
        board[row].reverse()



def transpose():
    global board

    board = [list(row) for row in zip(*board)]



def move_right():
    reverse()
    changed = move_left()
    reverse()
    return changed



def move_up():
    transpose()
    changed = move_left()
    transpose()
    return changed



def move_down():
    transpose()
    changed = move_right()
    transpose()
    return changed



def check_win():
    for row in board:
        if 2048 in row:
            return True

    return False



def can_move():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if board[row][col] == 0:
                return True

            if col < GRID_SIZE - 1 and board[row][col] == board[row][col + 1]:
                return True

            if row < GRID_SIZE - 1 and board[row][col] == board[row + 1][col]:
                return True

    return False



def game_over(message):
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(180)
    overlay.fill(BLACK)

    screen.blit(overlay, (0, 0))

    text = font.render(message, True, WHITE)
    score_text = small_font.render(f"Final Score: {score}", True, WHITE)

    screen.blit(text, (WIDTH // 2 - 120, HEIGHT // 2 - 40))
    screen.blit(score_text, (WIDTH // 2 - 90, HEIGHT // 2 + 20))

    pygame.display.update()
    pygame.time.delay(4000)

    pygame.quit()
    sys.exit()


# Start with two tiles
add_new_tile()
add_new_tile()

# Main game loop
while True:
    moved = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moved = move_left()

            elif event.key == pygame.K_RIGHT:
                moved = move_right()

            elif event.key == pygame.K_UP:
                moved = move_up()

            elif event.key == pygame.K_DOWN:
                moved = move_down()

            if moved:
                add_new_tile()

    # Win check
    if check_win():
        game_over("YOU REACHED 2048!")

    # Lose check
    if not can_move():
        game_over("GAME OVER")

    # Draw
    draw_board()

    pygame.display.update()
    clock.tick(60)
