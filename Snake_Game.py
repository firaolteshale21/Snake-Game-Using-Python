import curses
import time
import random

# Initialize the screen
screen = curses.initscr()
curses.cbreak()
screen.keypad(True)
screen.nodelay(True)  # Make getch() non-blocking
screen.timeout(100)  # Refresh screen every 100ms

# Game variables
snake = [(5, 5), (5, 4), (5, 3)]
direction = curses.KEY_RIGHT
food = (random.randint(1, 18), random.randint(1, 58))
score = 0

def draw_snake(screen, snake):
    for y, x in snake:
        screen.addch(y, x, '#')

def draw_food(screen, food):
    y, x = food
    screen.addch(y, x, '*')

# Main game loop
while True:
    screen.clear()
    draw_snake(screen, snake)
    draw_food(screen, food)
    screen.addstr(0, 2, f'Score: {score} ')
    screen.refresh()

    # Get user input
    key = screen.getch()
    if key in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
        direction = key

    # Update snake position
    head = snake[0]
    if direction == curses.KEY_UP:
        new_head = (head[0] - 1, head[1])
    elif direction == curses.KEY_DOWN:
        new_head = (head[0] + 1, head[1])
    elif direction == curses.KEY_LEFT:
        new_head = (head[0], head[1] - 1)
    elif direction == curses.KEY_RIGHT:
        new_head = (head[0], head[1] + 1)

    # Insert new head and remove tail
    snake.insert(0, new_head)
    if new_head == food:
        score += 1
        food = (random.randint(1, 18), random.randint(1, 58))
    else:
        snake.pop()

    # Check for collisions
    if (new_head[0] in [0, 19] or new_head[1] in [0, 59] or new_head in snake[1:]):
        break

# End the game
curses.endwin()
print(f'Game Over! Your score was {score}')
