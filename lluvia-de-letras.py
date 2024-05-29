import sys
import os
import pygame
from random import choice, randrange
from string import ascii_lowercase

# Check if we're running in a PyInstaller bundle
if getattr(sys, 'frozen', False):
    application_path = sys._MEIPASS
else:
    application_path = os.path.dirname(os.path.abspath(__file__))

targets = []
letters = []
score = 0
FONT_SIZE = 32  # Increase the font size
SPEED = 0.5  # Decrease the speed

# Initialize the mixer and pygame module
pygame.init()

# Create a screen
screen = pygame.display.set_mode((800, 600))

# Set the title of the screen
pygame.display.set_caption("Lluvia de letras")

# Load the sounds
sounds = {letter: pygame.mixer.Sound(
    os.path.join(application_path, 'sonidos', f'{letter}.wav')) for letter in ascii_lowercase}

font = pygame.font.Font('freesansbold.ttf', FONT_SIZE)

def draw():
    """Draw letters and score."""
    screen.fill((0, 0, 0))

    for target, letter in zip(targets, letters):
        text = font.render(letter, True, (255, 255, 255))
        screen.blit(text, target)

    # Draw score
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (200, 200))

    pygame.display.update()

def move():
    """Move letters."""
    global targets
    if randrange(20) == 0:
        x = randrange(-150, 150)
        target = pygame.Vector2(x, 200)
        targets.append(target)
        letter = choice(ascii_lowercase)
        letters.append(letter)

        # Play the sound for the new letter
        sounds[letter].play()

    targets = [target - pygame.Vector2(0, SPEED) for target in targets]  # Decrease the speed

    draw()

    targets = [target for target in targets if -200 < target.x < 200 and -200 < target.y < 200]

    pygame.time.set_timer(pygame.USEREVENT, 100)

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
    running = True
    pygame.time.set_timer(pygame.USEREVENT, 100)  # Move this line here
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key >= pygame.K_a and event.key <= pygame.K_z:
                    press(chr(event.key - pygame.K_a + ord('a')))
            elif event.type == pygame.USEREVENT:
                move()
except Exception as e:
    print(e)
    input('Press enter to exit...')
finally:
    pygame.quit()