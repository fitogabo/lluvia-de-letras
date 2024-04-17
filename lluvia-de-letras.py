import sys
import os
import pygame
from random import choice, randrange
from string import ascii_lowercase
from turtle import *
from freegames import vector

# Check if we're running in a PyInstaller bundle
if getattr(sys, 'frozen', False):
    application_path = sys._MEIPASS
else:
    application_path = os.path.dirname(os.path.abspath(__file__))

targets = []
letters = []
score = 0

# Create a screen
screen = Screen()

# Set the title of the screen
screen.title("Lluvia de letras")


def inside(point):
    """Return True if point on screen."""
    return -200 < point.x < 200 and -200 < point.y < 200


def draw():
    """Draw letters and score."""
    clear()

    for target, letter in zip(targets, letters):
        goto(target.x, target.y)
        write(letter, align='center', font=('Consolas', 20, 'normal'))

    # Draw score
    goto(200, 200)
    write("Score: " + str(score), align='right',
          font=('Consolas', 20, 'normal'))

    update()


# Initialize the mixer module
pygame.mixer.init()

# Load the sounds
sounds = {letter: pygame.mixer.Sound(
    os.path.join(sys._MEIPASS, 'sonidos', f'{letter}.wav')) for letter in ascii_lowercase}


def move():
    """Move letters."""
    if randrange(20) == 0:
        x = randrange(-150, 150)
        target = vector(x, 200)
        targets.append(target)
        letter = choice(ascii_lowercase)
        letters.append(letter)

        # Play the sound for the new letter
        sounds[letter].play()

    for target in targets:
        target.y -= 1

    draw()

    for target in targets:
        if not inside(target):
            return

    ontimer(move, 100)


def press(key):
    """Press key."""
    global score

    if key in letters:
        score += 1
        pos = letters.index(key)
        del targets[pos]
        del letters[pos]
    else:
        score -= 1

    print('Score:', score)


try:
    setup(420, 420, 370, 0)
    hideturtle()
    up()
    tracer(False)
    listen()
    for letter in ascii_lowercase:
        onkey(lambda letter=letter: press(letter), letter)
    move()
    done()
except Exception as e:
    print(e)
    input('Press enter to exit...')
