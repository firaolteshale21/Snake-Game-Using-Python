import curses
import time
import random

def main(screen):
    # Set up the screen
    curses.curs_set(0)  # Hide the cursor
    screen.nodelay(1)   # Make getch() non-blocking
    screen.timeout(100) # Refresh screen every 100ms

    # Get screen dimensions
    sh, sw = screen.getmaxyx()

    # Game variables
    snake = [(sh // 2, sw // 2), (sh // 2, sw // 2 - 1), (sh // 2, sw // 2 - 2)]
    direction = curses.KEY_RIGHT
    food = (random.randint(1, sh-2), random.randint(1, sw-2))
    score = 0

    def draw_snake(screen, snake):
        for y, x in snake:
            screen.addch(y, x, '*')

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
            food = (random.randint(1, sh-2), random.randint(1, sw-2))
        else:
            snake.pop()

        # Check for collisions
        if (new_head[0] in [0, sh-1] or new_head[1] in [0, sw-1] or new_head in snake[1:]):
            break

    # End the game
    curses.endwin()
    print(f'Game Over! Your score was {score}')

# Run the game
curses.wrapper(main)
