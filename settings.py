import pygame
#from main import GAME_SPEED

with open("settings_config/settings_screen.txt", 'r') as datei:
# Den gesamten Inhalt der Datei lesen
    inhalt = int(datei.read())


if inhalt == 0:
    SCREEN_HEIGHT = 1080
    SCREEN_WIDTH = 1920
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

elif inhalt == 1:
    SCREEN_HEIGHT = 1440
    SCREEN_WIDTH = 2560
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def screen_update():

    with open("settings_config/settings_screen.txt", 'r') as datei:
    # Den gesamten Inhalt der Datei lesen
        inhalt = int(datei.read())


    if inhalt == 0:
        SCREEN_HEIGHT = 1080
        SCREEN_WIDTH = 1920
        SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    elif inhalt == 1:
        SCREEN_HEIGHT = 1440
        SCREEN_WIDTH = 2560
        SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))





pygame.display.set_caption("Chrome Dino Runner")

Ico = pygame.image.load("assets/DinoWallpaper.png")
pygame.display.set_icon(Ico)

FONT_COLOR=(0,0,0)

GAME_SPEED = 15

