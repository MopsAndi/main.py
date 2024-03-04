from resources import RUNNING
import pygame
import random
import threading
from settings import SCREEN_WIDTH, SCREEN, SCREEN_HEIGHT, GAME_SPEED
from dinosaur import Dinosaur
from dinosaur import Dinosaur_Skin1_Bird
from dinosaur import Dinosaur_Skin2_Duck
from cloud import Cloud

from obstacles import SmallCactus, LargeCactus, Bird
from powerup import Powerup_1, Double_Points1

from resources import BG, SMALL_CACTUS, LARGE_CACTUS, BIRD
from resources import DOUBLE_POINTS

from menu_icons import Background_Menu_1
from menu_icons import Vanilla_GM, Vanilla_GM_SELECTED, Chellenger_GM_SELECTED, Chellenger_GM_UNSELECTED, Multiplayer_GM_SELECTED, Multiplayer_GM_UNSELECTED, Test, Settings_Icon_Selected, Settings_Icon_Unselected
from menu_icons import Dino_Shop_Icon_Selected, Dino_Shop_Icon_Unselected , Obstacle_Shop_Icon_Selected, Obstacle_Shop_Icon_Unselected, Bird_Shop_Icon_Selected, Bird_Shop_Icon_Unselected, Track_Shop_Icon_Selected, Track_Shop_Icon_Unselected, Power_Up_Shop_Icon_Selected, Power_Up_Shop_Icon_Unselected
from menu_icons import Blank_Shop_Icon_Unselected, Blank_Shop_Icon_Selected, Stats_Shop_Icon_Static, Buy_Button_Shop_Icon_Unselected, Buy_Button_Shop_Icon_Selected, Buy_Button_Shop_Icon_Pressed
from menu_icons import Dino1_Shop_Icon_Unselected, Dino1_Shop_Icon_Selected, Dino2_Shop_Icon_Unselected, Dino2_Shop_Icon_Selected, Dino3_Shop_Icon_Unselected, Dino3_Shop_Icon_Selected, Dino4_Shop_Icon_Unselected, Dino4_Shop_Icon_Selected, Dino5_Shop_Icon_Unselected, Dino5_Shop_Icon_Selected
from menu_icons import Obstacle1_Shop_Icon_Unselected, Obstacle1_Shop_Icon_Selected, Obstacle2_Shop_Icon_Unselected, Obstacle2_Shop_Icon_Selected, Obstacle3_Shop_Icon_Unselected, Obstacle3_Shop_Icon_Selected, Obstacle4_Shop_Icon_Unselected, Obstacle4_Shop_Icon_Selected, Obstacle5_Shop_Icon_Unselected, Obstacle5_Shop_Icon_Selected
from menu_icons import Bird1_Shop_Icon_Unselected, Bird1_Shop_Icon_Selected, Bird2_Shop_Icon_Unselected, Bird2_Shop_Icon_Selected, Bird3_Shop_Icon_Unselected, Bird3_Shop_Icon_Selected, Bird4_Shop_Icon_Unselected, Bird4_Shop_Icon_Selected, Bird5_Shop_Icon_Unselected, Bird5_Shop_Icon_Selected
from menu_icons import Track1_Shop_Icon_Unselected, Track1_Shop_Icon_Selected, Track2_Shop_Icon_Unselected, Track2_Shop_Icon_Selected, Track3_Shop_Icon_Unselected, Track3_Shop_Icon_Selected, Track4_Shop_Icon_Unselected, Track4_Shop_Icon_Selected, Track5_Shop_Icon_Unselected, Track5_Shop_Icon_Selected
from menu_icons import Powerup1_Shop_Icon_Unselected, Powerup1_Shop_Icon_Selected, Powerup2_Shop_Icon_Unselected, Powerup2_Shop_Icon_Selected, Powerup3_Shop_Icon_Unselected, Powerup3_Shop_Icon_Selected, Powerup4_Shop_Icon_Unselected, Powerup4_Shop_Icon_Selected, Powerup5_Shop_Icon_Unselected, Powerup5_Shop_Icon_Selected
from menu_icons import Start_Game_Unselected, Start_Game_Selected, Shop_Icon_Selected, Shop_Icon_Unselected, Quit_Unselected, Quit_Selected, Inventory_Selected, Inventory_Unselected, Background_Main_Menu
from transition import Transition, Transition_left
from avatar_icon import DinosaurAvatarIcon, BirdAvatarIcon, DuckAvatarIcon
from dinosaur import Dinosaur_player2, Bird_player2, Duck_player2, Dinosaur_skin4
from pygame.locals import *
from datetime import datetime

from menu_icons import Inv_slot_Test_selected,Inv_slot_Test_unselected

from menu_icons import Inv_c_Slot_Selected_1, Inv_c_Slot_Unselected_1, Inv_c_Slot_Selected_2, Inv_c_Slot_Unselected_2,Inv_c_Slot_Selected_3, Inv_c_Slot_Unselected_3, Inv_c_Slot_Selected_4, Inv_c_Slot_Unselected_4, Inv_c_Slot_Selected_5, Inv_c_Slot_Unselected_5, Inv_c_Slot_Selected_6, Inv_c_Slot_Unselected_6
from menu_icons import Inv_c_Slot_Selected_7, Inv_c_Slot_Unselected_7, Inv_c_Slot_Selected_8, Inv_c_Slot_Unselected_8,Inv_c_Slot_Selected_9, Inv_c_Slot_Unselected_9, Inv_c_Slot_Selected_10, Inv_c_Slot_Unselected_10, Inv_c_Slot_Selected_11, Inv_c_Slot_Unselected_11, Inv_c_Slot_Selected_12, Inv_c_Slot_Unselected_12

from settings import  screen_update
# Initialize Pygame
pygame.init()
pygame.mixer.init()

import time
import threading

def handle_controller_input():
    # Initialize pygame
    pygame.init()

    # Initialize the joystick
    pygame.joystick.init()
    joystick_count = pygame.joystick.get_count()

    if joystick_count == 0:
        print("No joystick detected.")
        return

    # Get the first joystick
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    # Variables to track button states
    a_button_pressed = False
    b_button_pressed = False
    up_pressed = False
    down_pressed = False
    left_pressed = False
    right_pressed = False

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        # Check for joystick input
        left_stick_x = joystick.get_axis(0)
        left_stick_y = joystick.get_axis(1)

        # Threshold for stick movement
        if abs(left_stick_x) > 0.5:
            if left_stick_x > 0 and not right_pressed:
                print("Move Right")
                # Perform move right action here
                pygame.event.post(pygame.event.Event(KEYDOWN, key=K_RIGHT))
                right_pressed = True
            elif left_stick_x < 0 and not left_pressed:
                print("Move Left")
                # Perform move left action here
                pygame.event.post(pygame.event.Event(KEYDOWN, key=K_LEFT))
                left_pressed = True
        else:
            right_pressed = False
            left_pressed = False

        if abs(left_stick_y) > 0.5:
            if left_stick_y > 0 and not down_pressed:
                print("Move Down")
                # Perform move down action here
                pygame.event.post(pygame.event.Event(KEYDOWN, key=K_DOWN))
                down_pressed = True
            elif left_stick_y < 0 and not up_pressed:
                print("Move Up")
                # Perform move up action here
                pygame.event.post(pygame.event.Event(KEYDOWN, key=K_UP))
                up_pressed = True
        else:
            down_pressed = False
            up_pressed = False

        # Check for button input
        for i in range(joystick.get_numbuttons()):
            if joystick.get_button(i):
                if i == 0 and not a_button_pressed:
                    print("A button pressed!")
                    # Perform Enter action here
                    pygame.event.post(pygame.event.Event(KEYDOWN, key=K_RETURN))
                    a_button_pressed = True
                elif i == 1 and not b_button_pressed:
                    print("B button pressed!")
                    # Perform Backspace action here
                    pygame.event.post(pygame.event.Event(KEYDOWN, key=K_BACKSPACE))
                    b_button_pressed = True
            else:
                if i == 0:
                    a_button_pressed = False
                elif i == 1:
                    b_button_pressed = False

        pygame.time.Clock().tick(30)  # Limit to 60 frames per second

controller_thread = threading.Thread(target=handle_controller_input)
controller_thread.start()

# List to store obstacles
obstacles = []

transition = Transition()
transition_left = Transition_left()

## Variablen dass Bilder Gerendert werden für "selection Screen" (un/selected)
startgameselected = Start_Game_Selected()
startgameunselected = Start_Game_Unselected()
shopiconselected = Shop_Icon_Selected()
shopiconunselected = Shop_Icon_Unselected()
quitselected = Quit_Selected()
quitunselected = Quit_Unselected()
invselected = Inventory_Selected()
invunselected = Inventory_Unselected()
bgmainmenue = Background_Main_Menu()
bgmenue1 = Background_Menu_1()

dinoblink = DinosaurAvatarIcon()
birdblink = BirdAvatarIcon()
duckblink = DuckAvatarIcon()

settings_selected = Settings_Icon_Selected()
settings_unselected = Settings_Icon_Unselected()

invtestunse = Inv_slot_Test_unselected()
invtestse = Inv_slot_Test_selected()

menu_sound_effekt = pygame.mixer.Sound('assets/Other/menu_sound.mp3')
musi_test_sound_effekt = pygame.mixer.Sound('assets/Other/menu_sound.mp3')
#musi_test.mp3

with open("skin_selection.txt", 'r') as f:
    skin_selection = int(f.read())

def main_menu(joystick=None):
    global shopselected,skin_selection

    shopselected = 0



    run = True
    selected = 0  # 0 for 'Start Game', 1 for 'Quit'

    while run:
        bgmainmenue.draw(SCREEN)  # Background for the menu
        test.draw(SCREEN)

        if skin_selection == 0:
            dinoblink.draw(SCREEN)
            dinoblink.update()
        elif skin_selection == 1:
            birdblink.draw(SCREEN)
            birdblink.update()
        elif skin_selection == 2:
            duckblink.draw(SCREEN)
            duckblink.update()

        font = pygame.font.Font("assets/Other/gothic_pixel.ttf", 80)
        title = font.render("", True, FONT_COLOR)

        # Options text
        if selected == 0:
            startgameselected.draw(SCREEN)
            shopiconunselected.draw(SCREEN)
            quitunselected.draw(SCREEN)
            invunselected.draw(SCREEN)
            settings_unselected.draw(SCREEN)


        if selected == 1:

            startgameunselected.draw(SCREEN)
            shopiconselected.draw(SCREEN)
            quitunselected.draw(SCREEN)
            invunselected.draw(SCREEN)
            settings_unselected.draw(SCREEN)

        if selected == 2:

            startgameunselected.draw(SCREEN)
            shopiconunselected.draw(SCREEN)
            quitselected.draw(SCREEN)
            invunselected.draw(SCREEN)
            settings_unselected.draw(SCREEN)



        if selected == 4:

            startgameunselected.draw(SCREEN)
            shopiconunselected.draw(SCREEN)
            quitunselected.draw(SCREEN)
            invselected.draw(SCREEN)
            settings_unselected.draw(SCREEN)


        if selected == 5:

            startgameunselected.draw(SCREEN)
            shopiconunselected.draw(SCREEN)
            quitunselected.draw(SCREEN)
            invunselected.draw(SCREEN)
            settings_selected.draw(SCREEN)


        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        SCREEN.blit(title, title_rect)
        pygame.display.update()


        # Switch between the options
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    menu_sound_effekt.play()
                    if selected == 5:
                        selected = 2
                    else:
                        selected = (selected + 1) % 3

                elif event.key == pygame.K_UP:

                    menu_sound_effekt.play()
                    if selected == 5:
                        selected = 0
                    else:
                        selected = (selected - 1) % 3
                elif event.key == pygame.K_RIGHT:
                    menu_sound_effekt.play()
                    if selected == 5:
                        selected = 1
                    else:
                        selected = 4
                elif event.key == pygame.K_LEFT:
                    menu_sound_effekt.play()
                    if selected == 4:
                        selected = 1
                    else:
                        selected = 5

                elif event.key == pygame.K_RETURN:
                    if selected == 0:
                        run = False
                        start_game_selector_screen(joystick)
                    elif selected == 1:
                        ausblenden_test()
                        shop_screen(joystick)
                        quit()
                    elif selected == 2:
                        ausblenden_test()
                        pygame.quit()
                        quit()
                    elif selected == 4:
                        transition.update(SCREEN)
                        inventory_menu(joystick)
                        quit()
                    elif selected == 5:
                        transition_left.update(SCREEN)
                        settings_menu(joystick)
                        quit()


## Variablen dass Bilder Gerendert werden für "Gamemode selection Screen" (un/selected)
vanillagm = Vanilla_GM()
vanillagm_sellected = Vanilla_GM_SELECTED()
chellenger_sellected = Chellenger_GM_SELECTED()
chellenger_unsellected = Chellenger_GM_UNSELECTED()
multiplayer_sellected = Multiplayer_GM_SELECTED()
multiplayer_unsellected = Multiplayer_GM_UNSELECTED()


test = Test()


def ausblenden_test():
    ausblenden = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    for i in range(0, 60, 3):
        ausblenden.set_alpha(i)
        SCREEN.blit(ausblenden, (0, 0))
        pygame.display.flip()




def ausblenden_test():
    ausblenden = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    for i in range(0, 60, 3):
        ausblenden.set_alpha(i)
        SCREEN.blit(ausblenden, (0, 0))
        pygame.display.flip()
        pygame.time.delay(35)

## Variablen dass Bilder Gerendert werden für "Gamemode selection Screen" (un/selected)
# vanillagm = Vanilla_GM()




slot_un_1 = Inv_c_Slot_Unselected_1()
slot_se_1 = Inv_c_Slot_Selected_1()
slot_un_2 = Inv_c_Slot_Unselected_2()
slot_se_2 = Inv_c_Slot_Selected_2()
slot_un_3 = Inv_c_Slot_Unselected_3()
slot_se_3 = Inv_c_Slot_Selected_3()
slot_un_4 = Inv_c_Slot_Unselected_4()
slot_se_4 = Inv_c_Slot_Selected_4()
slot_un_5 = Inv_c_Slot_Unselected_5()
slot_se_5 = Inv_c_Slot_Selected_5()
slot_un_6 = Inv_c_Slot_Unselected_6()
slot_se_6 = Inv_c_Slot_Selected_6()

slot_un_7 = Inv_c_Slot_Unselected_7()
slot_se_7 = Inv_c_Slot_Selected_7()
slot_un_8 = Inv_c_Slot_Unselected_8()
slot_se_8 = Inv_c_Slot_Selected_8()
slot_un_9 = Inv_c_Slot_Unselected_9()
slot_se_9 = Inv_c_Slot_Selected_9()
slot_un_10 = Inv_c_Slot_Unselected_10()
slot_se_10 = Inv_c_Slot_Selected_10()
slot_un_11 = Inv_c_Slot_Unselected_11()
slot_se_11 = Inv_c_Slot_Selected_11()
slot_un_12 = Inv_c_Slot_Unselected_12()
slot_se_12 = Inv_c_Slot_Selected_12()

def inventory_menu(joystick=None):

    run = True
    selected = 0  # 0 for 'Start Game', 1 for 'Quit'

    while run:
        #SCREEN.fill((0, 0, 0))  # Black background for the menu
        bgmainmenue.draw(SCREEN)  # Background for the menu
        font = pygame.font.Font("assets/Other/gothic_pixel.ttf", 60)
        title = font.render("Inventory", True, FONT_COLOR)

        # Options text
        if selected == 5:
            slot_se_1.draw(SCREEN)
            slot_un_2.draw(SCREEN)
            slot_un_3.draw(SCREEN)
            slot_un_4.draw(SCREEN)
            slot_un_5.draw(SCREEN)
            slot_un_6.draw(SCREEN)

            slot_un_7.draw(SCREEN)
            slot_un_8.draw(SCREEN)
            slot_un_9.draw(SCREEN)
            slot_un_10.draw(SCREEN)
            slot_un_11.draw(SCREEN)
            slot_un_12.draw(SCREEN)

        if selected == 4:
            slot_un_1.draw(SCREEN)
            slot_se_2.draw(SCREEN)
            slot_un_3.draw(SCREEN)
            slot_un_4.draw(SCREEN)
            slot_un_5.draw(SCREEN)
            slot_un_6.draw(SCREEN)

            slot_un_7.draw(SCREEN)
            slot_un_8.draw(SCREEN)
            slot_un_9.draw(SCREEN)
            slot_un_10.draw(SCREEN)
            slot_un_11.draw(SCREEN)
            slot_un_12.draw(SCREEN)

        if selected == 3:
            slot_un_1.draw(SCREEN)
            slot_un_2.draw(SCREEN)
            slot_se_3.draw(SCREEN)
            slot_un_4.draw(SCREEN)
            slot_un_5.draw(SCREEN)
            slot_un_6.draw(SCREEN)

            slot_un_7.draw(SCREEN)
            slot_un_8.draw(SCREEN)
            slot_un_9.draw(SCREEN)
            slot_un_10.draw(SCREEN)
            slot_un_11.draw(SCREEN)
            slot_un_12.draw(SCREEN)

        if selected == 2:
            slot_un_1.draw(SCREEN)
            slot_un_2.draw(SCREEN)
            slot_un_3.draw(SCREEN)
            slot_se_4.draw(SCREEN)
            slot_un_5.draw(SCREEN)
            slot_un_6.draw(SCREEN)

            slot_un_7.draw(SCREEN)
            slot_un_8.draw(SCREEN)
            slot_un_9.draw(SCREEN)
            slot_un_10.draw(SCREEN)
            slot_un_11.draw(SCREEN)
            slot_un_12.draw(SCREEN)

        if selected == 1:
            slot_un_1.draw(SCREEN)
            slot_un_2.draw(SCREEN)
            slot_un_3.draw(SCREEN)
            slot_un_4.draw(SCREEN)
            slot_se_5.draw(SCREEN)
            slot_un_6.draw(SCREEN)

            slot_un_7.draw(SCREEN)
            slot_un_8.draw(SCREEN)
            slot_un_9.draw(SCREEN)
            slot_un_10.draw(SCREEN)
            slot_un_11.draw(SCREEN)
            slot_un_12.draw(SCREEN)

        if selected == 0:
            slot_un_1.draw(SCREEN)
            slot_un_2.draw(SCREEN)
            slot_un_3.draw(SCREEN)
            slot_un_4.draw(SCREEN)
            slot_un_5.draw(SCREEN)
            slot_se_6.draw(SCREEN)

            slot_un_7.draw(SCREEN)
            slot_un_8.draw(SCREEN)
            slot_un_9.draw(SCREEN)
            slot_un_10.draw(SCREEN)
            slot_un_11.draw(SCREEN)
            slot_un_12.draw(SCREEN)

        if selected == 11:
            slot_se_7.draw(SCREEN)
            slot_un_8.draw(SCREEN)
            slot_un_9.draw(SCREEN)
            slot_un_10.draw(SCREEN)
            slot_un_11.draw(SCREEN)
            slot_un_12.draw(SCREEN)

            slot_un_1.draw(SCREEN)
            slot_un_2.draw(SCREEN)
            slot_un_3.draw(SCREEN)
            slot_un_4.draw(SCREEN)
            slot_un_5.draw(SCREEN)
            slot_un_6.draw(SCREEN)

        if selected == 10:
            slot_un_7.draw(SCREEN)
            slot_se_8.draw(SCREEN)
            slot_un_9.draw(SCREEN)
            slot_un_10.draw(SCREEN)
            slot_un_11.draw(SCREEN)
            slot_un_12.draw(SCREEN)

            slot_un_1.draw(SCREEN)
            slot_un_2.draw(SCREEN)
            slot_un_3.draw(SCREEN)
            slot_un_4.draw(SCREEN)
            slot_un_5.draw(SCREEN)
            slot_un_6.draw(SCREEN)

        if selected == 9:
            slot_un_7.draw(SCREEN)
            slot_un_8.draw(SCREEN)
            slot_se_9.draw(SCREEN)
            slot_un_10.draw(SCREEN)
            slot_un_11.draw(SCREEN)
            slot_un_12.draw(SCREEN)

            slot_un_1.draw(SCREEN)
            slot_un_2.draw(SCREEN)
            slot_un_3.draw(SCREEN)
            slot_un_4.draw(SCREEN)
            slot_un_5.draw(SCREEN)
            slot_un_6.draw(SCREEN)

        if selected == 8:
            slot_un_7.draw(SCREEN)
            slot_un_8.draw(SCREEN)
            slot_un_9.draw(SCREEN)
            slot_se_10.draw(SCREEN)
            slot_un_11.draw(SCREEN)
            slot_un_12.draw(SCREEN)

            slot_un_1.draw(SCREEN)
            slot_un_2.draw(SCREEN)
            slot_un_3.draw(SCREEN)
            slot_un_4.draw(SCREEN)
            slot_un_5.draw(SCREEN)
            slot_un_6.draw(SCREEN)

        if selected == 7:
            slot_un_7.draw(SCREEN)
            slot_un_8.draw(SCREEN)
            slot_un_9.draw(SCREEN)
            slot_un_10.draw(SCREEN)
            slot_se_11.draw(SCREEN)
            slot_un_12.draw(SCREEN)

            slot_un_1.draw(SCREEN)
            slot_un_2.draw(SCREEN)
            slot_un_3.draw(SCREEN)
            slot_un_4.draw(SCREEN)
            slot_un_5.draw(SCREEN)
            slot_un_6.draw(SCREEN)

        if selected == 6:
            slot_un_7.draw(SCREEN)
            slot_un_8.draw(SCREEN)
            slot_un_9.draw(SCREEN)
            slot_un_10.draw(SCREEN)
            slot_un_11.draw(SCREEN)
            slot_se_12.draw(SCREEN)

            slot_un_1.draw(SCREEN)
            slot_un_2.draw(SCREEN)
            slot_un_3.draw(SCREEN)
            slot_un_4.draw(SCREEN)
            slot_un_5.draw(SCREEN)
            slot_un_6.draw(SCREEN)

        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        SCREEN.blit(title, title_rect)

        pygame.display.update()

        # Switch between the options
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    selected = (selected + 1) % 12
                    menu_sound_effekt.play()
                elif event.key == pygame.K_LEFT:
                    selected = (selected - 1) % 12
                    menu_sound_effekt.play()

                elif event.key == pygame.K_DOWN:
                    selected = (selected + 6) % 12
                    menu_sound_effekt.play()
                elif event.key == pygame.K_UP:
                    selected = (selected - 6) % 12
                    menu_sound_effekt.play()

                elif event.key == pygame.K_BACKSPACE:
                    transition_left.update(SCREEN)
                    main_menu(joystick)
                elif event.key == pygame.K_RETURN:
                    if selected == 0:
                        run = False
                        quit()
                    elif selected == 1:
                        quit()

def settings_menu(joystick=None):

    run = True
    selected = 0  # 0 for 'Start Game', 1 for 'Quit'

    while run:
        #SCREEN.fill((0, 0, 0))  # Black background for the menu
        bgmainmenue.draw(SCREEN)  # Background for the menu
        font = pygame.font.Font("assets/Other/gothic_pixel.ttf", 60)
        title = font.render("Settings", True, FONT_COLOR)

        # Options text
        if selected == 0:
            start_game = font.render("1920 1080 <-", True, FONT_COLOR)
            shop = font.render("Reset Game", True, FONT_COLOR)
            settings3text = font.render("2650 1440", True, FONT_COLOR)

        if selected == 1:
            start_game = font.render("1920 1080", True, FONT_COLOR)
            settings3text = font.render("2560 1440 <-", True, FONT_COLOR)
            shop = font.render("Reset Game", True, FONT_COLOR)

        if selected == 2:
            start_game = font.render("1920 1080", True, FONT_COLOR)
            settings3text = font.render("2650 1440", True, FONT_COLOR)
            shop = font.render("Reset Game <-", True, FONT_COLOR)


        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        start_game_rect = start_game.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2.5))
        settings3text_rect = settings3text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        shop_rect = shop.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 - 100))

        SCREEN.blit(title, title_rect)
        SCREEN.blit(start_game, start_game_rect)
        SCREEN.blit(shop, shop_rect)
        SCREEN.blit(settings3text, settings3text_rect)
        pygame.display.update()

        # Switch between the options
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % 3
                    menu_sound_effekt.play()
                elif event.key == pygame.K_UP:
                    selected = (selected - 1) % 3
                    menu_sound_effekt.play()
                elif event.key == pygame.K_BACKSPACE:
                    transition.update(SCREEN)
                    main_menu(joystick)
                elif event.key == pygame.K_RETURN:
                    if selected == 0:
                        with open("settings_config/settings_screen.txt", 'w') as datei:
                        # Den gesamten Inhalt der Datei lesen
                            datei.write(str(0))
                        screen_update()

                    elif selected == 1:
                        with open("settings_config/settings_screen.txt", 'w') as datei:
                        # Den gesamten Inhalt der Datei lesen
                            datei.write(str(1))
                        screen_update()

                    elif selected == 2:
                        resetgame_yes_no(joystick)
                        quit()



def start_game_selector_screen(joystick=None):
    run = True
    selected = 0  # 0 for 'Start Game', 1 for 'Quit'

    while run:
        #SCREEN.fill((0, 0, 0))  # Black background for the menu
        bgmenue1.draw(SCREEN)  # Background for the menu
        font = pygame.font.Font("assets/Other/gothic_pixel.ttf", 60)
        title = font.render("Choose Gamemode", True, FONT_COLOR)

        # Options text
        if selected == 0:
            mission_mode = font.render("Mission Mode <-", True, FONT_COLOR)
            chellenger_sellected.draw(SCREEN)
            singleplayer_mode = font.render("Singleplayer", True, FONT_COLOR)
            vanillagm.draw(SCREEN)
            multiplayer_mode = font.render("Multiplayer", True, FONT_COLOR)
            multiplayer_unsellected.draw(SCREEN)



        if selected == 1:
            mission_mode = font.render("Mission Mode", True, FONT_COLOR)
            chellenger_unsellected.draw(SCREEN)
            singleplayer_mode = font.render("-->Singleplayer<--", True, FONT_COLOR)
            vanillagm_sellected.draw(SCREEN)
            multiplayer_mode = font.render("Multiplayer", True, FONT_COLOR)
            multiplayer_unsellected.draw(SCREEN)



        if selected == 2:
            mission_mode = font.render("Mission Mode", True, FONT_COLOR)
            chellenger_unsellected.draw(SCREEN)
            singleplayer_mode = font.render("Singleplayer", True, FONT_COLOR)
            vanillagm.draw(SCREEN)
            multiplayer_mode = font.render("->Multiplayer", True, FONT_COLOR)
            multiplayer_sellected.draw(SCREEN)


        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4 - 100))
        mission_mode_rect = mission_mode.get_rect(center=(SCREEN_WIDTH // 2 - 410, SCREEN_HEIGHT // 1.2))
        singleplayer_mode_rect = singleplayer_mode.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.2))
        multiplayer_mode_rect = multiplayer_mode.get_rect(center=(SCREEN_WIDTH // 2 + 410, SCREEN_HEIGHT // 1.2))

        SCREEN.blit(title, title_rect)
        SCREEN.blit(mission_mode, mission_mode_rect)
        SCREEN.blit(singleplayer_mode, singleplayer_mode_rect)
        SCREEN.blit(multiplayer_mode, multiplayer_mode_rect)

        pygame.display.update()

        # Switch between the options
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                pygame.event.pump()
                if event.key == pygame.K_RIGHT:
                    selected = (selected + 1) % 3
                    menu_sound_effekt.play()
                elif event.key == pygame.K_LEFT:
                    selected = (selected - 1) % 3
                    menu_sound_effekt.play()
                elif event.key == pygame.K_BACKSPACE:
                    ausblenden_test()
                    main_menu(joystick)
                elif event.key == pygame.K_RETURN:
                    if selected == 0:
                        mission_menu(joystick)
                        pygame.quit()
                        quit()

                    elif selected == 1:
                        run = False
                        main(joystick)

                    elif selected == 2:
                        multiplayer_menu(joystick)
                        pygame.quit()
                        quit()


## Variablen dass Bilder Gerendert werden für "Gamemode selection Screen" (un/selected)
# vanillagm = Vanilla_GM()

def mission_menu(joystick=None):

    runmission = True
    selected = 0  # 0 for 'Start Game', 1 for 'Quit'

    while runmission:
        SCREEN.fill((0, 0, 0))  # Black background for the menu

        font = pygame.font.Font("assets/Other/gothic_pixel.ttf", 60)
        title = font.render("Mission Mode", True, FONT_COLOR)

        # Options text
        if selected == 0:
            start_game = font.render("Mission1 <-", True, FONT_COLOR)
            shop = font.render("Mission2", True, FONT_COLOR)
            quit_game = font.render("Mission3", True, FONT_COLOR)
        if selected == 1:
            start_game = font.render("Mission1", True, FONT_COLOR)
            shop = font.render("Mission2<-", True, FONT_COLOR)
            quit_game = font.render("Mission3", True, FONT_COLOR)
        if selected == 2:
            start_game = font.render("Mission1", True, FONT_COLOR)
            shop = font.render("Mission2", True, FONT_COLOR)
            quit_game = font.render("Mission3<-", True, FONT_COLOR)

        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        start_game_rect = start_game.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        shop_rect = shop.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5))
        quit_game_rect = quit_game.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.2))

        SCREEN.blit(title, title_rect)
        SCREEN.blit(start_game, start_game_rect)
        SCREEN.blit(shop, shop_rect)
        SCREEN.blit(quit_game, quit_game_rect)
        pygame.display.update()

        # Switch between the options
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % 3
                    menu_sound_effekt.play()
                elif event.key == pygame.K_UP:
                    selected = (selected - 1) % 3
                    menu_sound_effekt.play()
                elif event.key == pygame.K_BACKSPACE:
                    start_game_selector_screen(joystick)
                elif event.key == pygame.K_RETURN:
                    if selected == 0:
                        main_mission1(joystick)
                        runmission = False
                        quit()
                    elif selected == 1:
                        main_mission2(joystick)
                        quit()
                    elif selected == 2:
                        main_mission3(joystick)
                        quit()

## Variablen dass Bilder Gerendert werden für "Gamemode selection Screen" (un/selected)
# vanillagm = Vanilla_GM()

def multiplayer_menu(joystick=None):

    runmultiplayer = True
    selected = 0  # 0 for 'Start Game', 1 for 'Quit'

    while runmultiplayer:
        SCREEN.fill((0, 0, 0))  # Black background for the menu

        font = pygame.font.Font("assets/Other/gothic_pixel.ttf", 60)
        title = font.render("Multiplayer Mode", True, FONT_COLOR)

        # Options text
        if selected == 0:
            start_game = font.render("Co-op <-", True, FONT_COLOR)
            shop = font.render("Wettkampf", True, FONT_COLOR)

        if selected == 1:
            start_game = font.render("Co-op", True, FONT_COLOR)
            shop = font.render("Wettkampf<-", True, FONT_COLOR)


        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        start_game_rect = start_game.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        shop_rect = shop.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5))

        SCREEN.blit(title, title_rect)
        SCREEN.blit(start_game, start_game_rect)
        SCREEN.blit(shop, shop_rect)
        pygame.display.update()

        # Switch between the options
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % 2
                    menu_sound_effekt.play()
                elif event.key == pygame.K_UP:
                    selected = (selected - 1) % 2
                    menu_sound_effekt.play()
                elif event.key == pygame.K_BACKSPACE:
                    start_game_selector_screen(joystick)
                elif event.key == pygame.K_RETURN:
                    if selected == 0:
                        main_Coop(joystick)
                        runmultiplayer = False
                        quit()
                    elif selected == 1:
                        main_Wettkampf(joystick)
                        quit()

money_render_plus = 0

def death_screen_restart_select_singleplayer(money_render_plus,joystick=None):
    run = True
    selected = 0  # 0 for 'Start Game', 1 for 'Quit'
    global points_value
    points_value = 0.1
    musi_test_sound_effekt.stop()


    while run:

        font = pygame.font.Font("assets/Other/gothic_pixel.ttf", 45)  # Set the font and size for the text.
        pygame.display.update()  # Update the entire screen with everything drawn.
        FONT_COLOR69 = (0, 255, 000)

        # Options text
        if selected == 0:

            restart_game = font.render("Retry <-", True, FONT_COLOR)
            main_screen = font.render("Back to Main Menu", True, FONT_COLOR)
            SCREEN.fill((128, 128, 128))

        else:

            restart_game = font.render("Retry", True, FONT_COLOR)
            main_screen = font.render("Back to Main Menu<-", True, FONT_COLOR)
            SCREEN.fill((128, 128, 128))


        score = font.render("Your Score: " + str(points), True, FONT_COLOR)
        money1 = font.render("Your Money: " + str(money), True, FONT_COLOR)
        money_render_plus = round(money_render_plus,2)
        moneyplus = font.render("+ " + str(money_render_plus) +" $", True, FONT_COLOR69)


        money1Rect = money1.get_rect()
        money1Rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 80)
        SCREEN.blit(money1, money1Rect)

        moneyplusRect = moneyplus.get_rect()
        moneyplusRect.center = (SCREEN_WIDTH // 2 + 130, SCREEN_HEIGHT // 2 + 115)
        SCREEN.blit(moneyplus, moneyplusRect)


        scoreRect = score.get_rect()
        scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
        SCREEN.blit(score, scoreRect)

            # Draw the score on the screen.

        with open("highscore.txt", 'r') as datei:
                # Den gesamten Inhalt der Datei lesen

            inhalt = datei.read()

        if points > float(inhalt):
            with open("highscore.txt", 'w') as datei:
                datei.write(str(points))

        score = font.render("Your Highscore: " + str(inhalt), True, FONT_COLOR)


        # Render the text and position it on the screen.
        scoreRect = score.get_rect()
        scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 6)
        SCREEN.blit(score, scoreRect)
        # Draw the text on the screen.
        # Display an image representing the game character.
        SCREEN.blit(RUNNING[0], (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 140))

        restart_game_rect = restart_game.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150))
        main_screen_rect = main_screen.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 200))

        SCREEN.blit(restart_game, restart_game_rect)
        SCREEN.blit(main_screen, main_screen_rect)

        pygame.display.update()

        # Switch between the options
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % 2
                    menu_sound_effekt.play()
                elif event.key == pygame.K_UP:
                    selected = (selected - 1) % 2
                    menu_sound_effekt.play()
                elif event.key == pygame.K_RETURN:
                    if selected == 0:
                        run = False
                        main(joystick)
                    elif selected == 1:
                        ausblenden_test()
                        main_menu(joystick)
                        quit()


def death_screen_restart_select_coop(money_render_plus,joystick=None):
    run = True
    FONT_COLOR69 = (0, 255, 000)
    selected = 0  # 0 for 'Start Game', 1 for 'Quit'
    with open("money.txt", 'r') as f:
        old_money = float(f.read())

        money = old_money + points * 0.1
        money = round(money, 2)
        money_render_plus = points * 0.1

        with open("money.txt", 'w') as f:
            f.write(str(money))
    money_render_plus = round(money_render_plus, 2)
    while run:

        font = pygame.font.Font("assets/Other/gothic_pixel.ttf", 55)  # Set the font and size for the text.
        pygame.display.update()  # Update the entire screen with everything drawn.

        # Options text
        if selected == 0:

            restart_game = font.render("Retry <-", True, FONT_COLOR)
            main_screen = font.render("Back to Main Menu", True, FONT_COLOR)
            SCREEN.fill((128, 128, 128))

        else:

            restart_game = font.render("Retry", True, FONT_COLOR)
            main_screen = font.render("Back to Main Menu<-", True, FONT_COLOR)
            SCREEN.fill((128, 128, 128))



        score = font.render("Your Score: " + str(points), True, FONT_COLOR)
        money1 = font.render("Your Money: " + str(money), True, FONT_COLOR)
        moneyplus = font.render("+ " + str(money_render_plus) + " $", True, FONT_COLOR69)

        money1Rect = money1.get_rect()
        money1Rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 80)
        SCREEN.blit(money1, money1Rect)

        scoreRect = score.get_rect()
        scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
        SCREEN.blit(score, scoreRect)

        moneyplusRect = moneyplus.get_rect()
        moneyplusRect.center = (SCREEN_WIDTH // 2 + 130, SCREEN_HEIGHT // 2 + 115)
        SCREEN.blit(moneyplus, moneyplusRect)


            # Draw the score on the screen.

        with open("highscore.txt", 'r') as datei:
                # Den gesamten Inhalt der Datei lesen

            inhalt = datei.read()

        if points > float(inhalt):
            with open("highscore.txt", 'w') as datei:
                datei.write(str(points))

        score = font.render("Your Highscore: " + str(inhalt), True, FONT_COLOR)


        # Render the text and position it on the screen.
        scoreRect = score.get_rect()
        scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 6)
        SCREEN.blit(score, scoreRect)
        # Draw the text on the screen.
        # Display an image representing the game character.
        SCREEN.blit(RUNNING[0], (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 140))

        restart_game_rect = restart_game.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150))
        main_screen_rect = main_screen.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 200))

        SCREEN.blit(restart_game, restart_game_rect)
        SCREEN.blit(main_screen, main_screen_rect)

        pygame.display.update()

        # Switch between the options
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % 2
                    menu_sound_effekt.play()
                elif event.key == pygame.K_UP:
                    selected = (selected - 1) % 2
                    menu_sound_effekt.play()
                elif event.key == pygame.K_RETURN:
                    if selected == 0:
                        run = False
                        main_Coop(joystick)
                    elif selected == 1:
                        ausblenden_test()
                        main_menu(joystick)
                        quit()


def death_screen_restart_select_wettkampf(joystick=None):
    run = True
    selected = 0  # 0 for 'Start Game', 1 for 'Quit'
    money_render_plus = points * 0.1
    money_render_plus = round(money_render_plus,2)

    while run:

        round(points, 1)
        round(points2, 1)
        font1 = pygame.font.Font("assets/Other/gothic_pixel.ttf", 160)
        font = pygame.font.Font("assets/Other/gothic_pixel.ttf", 55)  # Set the font and size for the text.
        pygame.display.update()  # Update the entire screen with everything drawn.

        # Options text
        if selected == 0:

            restart_game = font.render("Rematch <-", True, FONT_COLOR)
            main_screen = font.render("Back to Main Menu", True, FONT_COLOR)
            SCREEN.fill((128, 128, 128))

        else:

            restart_game = font.render("Rematch", True, FONT_COLOR)
            main_screen = font.render("Back to Main Menu<-", True, FONT_COLOR)
            SCREEN.fill((128, 128, 128))


        if points > points2:
            winner = font1.render("Player1 Won the game", True, FONT_COLOR)
            winnerRect = winner.get_rect()
            winnerRect.center = (SCREEN_WIDTH // 2 , SCREEN_HEIGHT // 2 - 350)
            SCREEN.blit(winner, winnerRect)

        else:
            winner2 = font1.render("Player2 Won the Game", True, FONT_COLOR)
            winner2Rect = winner2.get_rect()
            winner2Rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 350)
            SCREEN.blit(winner2, winner2Rect)

        score = font.render("Player1 Score: " + str(points), True, FONT_COLOR)
        score2 = font.render("Player2 Score: " + str(points2), True, FONT_COLOR)

        scoreRect = score.get_rect()
        scoreRect.center = (SCREEN_WIDTH // 2 + 250, SCREEN_HEIGHT // 2 + 50)
        SCREEN.blit(score, scoreRect)

        score2Rect = score2.get_rect()
        score2Rect.center = (SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT // 2 + 50)
        SCREEN.blit(score2, score2Rect)

        # Draw the score on the screen.




        # Draw the text on the screen.
        # Display an image representing the game character.
        SCREEN.blit(RUNNING[0], (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 140))
        restart_game_rect = restart_game.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150))
        main_screen_rect = main_screen.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 200))

        SCREEN.blit(restart_game, restart_game_rect)
        SCREEN.blit(main_screen, main_screen_rect)

        pygame.display.update()

        # Switch between the options
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % 2
                    menu_sound_effekt.play()
                elif event.key == pygame.K_UP:
                    selected = (selected - 1) % 2
                    menu_sound_effekt.play()
                elif event.key == pygame.K_RETURN:
                    if selected == 0:
                        run = False
                        main_Wettkampf(joystick)
                    elif selected == 1:
                        ausblenden_test()
                        main_menu(joystick)
                        quit()





### Ist der %-ige gewinn von Score in Geld

skin_selection = 0
with open("skin_selection.txt", 'r') as f:
    skin_selection = int(f.read())

def main(joystick=None):
    # Global variables for game settings
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles, money , points_value, skin_selection, powerups, FONT_COLOR

    # Set initial game state
    run = True
    clock = pygame.time.Clock()
    musi_test_sound_effekt.play()

    if skin_selection == 0:
        player = Dinosaur()
    elif skin_selection == 1:
        player = Dinosaur_Skin1_Bird()
    elif skin_selection == 2:
        player = Dinosaur_Skin2_Duck()

    obstacles = []
    powerups = []

    cloud = Cloud()
    game_speed = GAME_SPEED
    x_pos_bg = 0
    y_pos_bg = 750
    points = 0
    font = pygame.font.Font("assets/Other/gothic_pixel.ttf", 35)
    font2 = pygame.font.Font("assets/Other/gothic_pixel.ttf", 55)
    death_count = 0
    pause = False
    money = 0
    double_points_time = 0

    # Function to handle scoring (currently empty)

    def randerscore():
        global points, score, game_speed, FONT_COLOR, FONT_COLOR3
        FONT_COLOR3 = (255, 000, 000)
        score = font.render("Score: " + str(points), True, FONT_COLOR)
        if double_points_time >= 0:
            score = font2.render("Score: " + str(points), True, FONT_COLOR3)
        scoreRect = score.get_rect()
        scoreRect.midleft = (SCREEN_WIDTH - 1900, SCREEN_HEIGHT - 650)
        SCREEN.blit(score, scoreRect)
        pygame.display.update()

    # Function to handle background movement
    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            x_pos_bg = 0
        x_pos_bg -= game_speed

    # Function to unpause the game
    def unpause():
        nonlocal pause, run
        pause = False
        run = True

    # Function to pause the game
    def paused():
        nonlocal pause
        pause = True
        font = pygame.font.Font("assets/Other/gothic_pixel.ttf", 60)
        text = font.render("Game Paused, Press 'Esc' to Unpause", True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3)
        SCREEN.blit(text, textRect)
        pygame.display.update()

        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    unpause()

    # Main game loop
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                paused()

        # Fill screen with white color

        def score():
            global points, game_speed, points_value, FONT_COLOR
            points += points_value
            points = round(points, 1)

            # from datetime import datetime

        def is_dark_mode():
            now = datetime.now()
            if now.hour >= 22 or now.hour < 6:
                return False
            return True

        dark_mode = is_dark_mode()

        if dark_mode:
            SCREEN.fill((255, 255, 255))
            FONT_COLOR = (0, 0, 0)

        else:
            SCREEN.fill((30, 30, 30))
            FONT_COLOR = (255, 255, 255)

        is_dark_mode()



        # Get user input
        userInput = pygame.key.get_pressed()
        # Update and draw player and cloud

        background()

        player.draw(SCREEN)
        player.update(userInput)
        cloud.draw(SCREEN)
        cloud.update()


        # Handle obstacles
        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(BIRD))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update(obstacles)
            if player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(0)
                death_count += 1
                menu(death_count)


        # Handle Powerups
        items_reading()
        if len(powerups) == 0:
            if double_points_unlocked_checked == 1:
                if random.randint(0, 2) == 0:
                    powerups.append(Double_Points1(DOUBLE_POINTS))

        for powerup in powerups:
            powerup.draw(SCREEN)
            powerup.update(powerups)
            if player.dino_rect.colliderect(powerup.rect):
                pygame.time.delay(0)
                double_points_time = 100
                points_value *= 2
                powerups = []

        ##Doublepoints timer
        double_points_time -= 1
        if double_points_time <= 0:
            points_value = 0.1


        # Update background and score and rander score
        score()
        randerscore()
        # Update display and tick clock
        clock.tick(60)
        pygame.display.update()

def main_mission1(joystick=None):
    # Global variables for game settings
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles, money , points_value, skin_selection

    # Set initial game state
    run = True
    clock = pygame.time.Clock()

    if skin_selection == 0:
        player = Dinosaur()
    elif skin_selection == 1:
        player = Dinosaur_Skin1_Bird()
    elif skin_selection == 2:
        player = Dinosaur_Skin2_Duck()

    obstacles = []
    cloud = Cloud()
    game_speed = GAME_SPEED
    x_pos_bg = 0
    y_pos_bg = 750
    points = 0
    font = pygame.font.Font("assets/Other/gothic_pixel.ttf", 35)
    death_count = 0
    pause = False
    money = 0
    points_value = 0.1


    # Function to handle scoring (currently empty)
    def score():
        global points, game_speed, points_value
        points +=  points_value
        points = round(points,1)

    def randerscore():
        global points, score, game_speed, FONT_COLOR2
        score = font.render("Score: " + str(points), True, FONT_COLOR2)
        scoreRect = score.get_rect()
        scoreRect.midleft = (10, SCREEN_HEIGHT - 650)
        SCREEN.blit(score, scoreRect)
        pygame.display.update()

    # Function to handle background movement
    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            x_pos_bg = 0
        x_pos_bg -= game_speed

    # Function to unpause the game
    def unpause():
        nonlocal pause, run
        pause = False
        run = True

    # Function to pause the game
    def paused():
        nonlocal pause
        pause = True
        font = pygame.font.Font("assets/Other/gothic_pixel.ttf", 60)
        text = font.render("Game Paused, Press 'Esc' to Unpause", True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3)
        SCREEN.blit(text, textRect)
        pygame.display.update()

        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    unpause()

    # Main game loop
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                paused()

        # Fill screen with white color
        SCREEN.fill((255, 255, 255))
        # Get user input
        userInput = pygame.key.get_pressed()

        # Update and draw player and cloud

        background()

        player.draw(SCREEN)
        player.update(userInput)
        cloud.draw(SCREEN)
        cloud.update()


        # Handle obstacles
        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(BIRD))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update(obstacles)
            if player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(0)
                death_count += 1
                death_mission1()

        # Update background and score and rander score
        score()
        randerscore()
        # Update display and tick clock
        clock.tick(60)
        pygame.display.update()

def death_mission1(joystick=None):

    run = True
    FONT_COLOR69 = (0, 255, 000)
    selected = 0  # 0 for 'Start Game', 1 for 'Quit'
    with open("money.txt", 'r') as f:
        old_money = float(f.read())

        money = old_money + points * 0.1
        money = round(money, 2)
        money_render_plus = points * 0.1
        money_render_plus = round(money_render_plus,2)
        with open("money.txt", 'w') as f:
            f.write(str(money))

    while run:

        font = pygame.font.Font("assets/Other/gothic_pixel.ttf", 55)  # Set the font and size for the text.
        pygame.display.update()  # Update the entire screen with everything drawn.

        # Options text
        if selected == 0:

            restart_game = font.render("Retry <-", True, FONT_COLOR)
            main_screen = font.render("Back to Main Menu", True, FONT_COLOR)
            SCREEN.fill((128, 128, 128))

        else:

            restart_game = font.render("Retry", True, FONT_COLOR)
            main_screen = font.render("Back to Main Menu<-", True, FONT_COLOR)
            SCREEN.fill((128, 128, 128))



        score = font.render("Your Score: " + str(points), True, FONT_COLOR)
        money1 = font.render("Your Money: " + str(money), True, FONT_COLOR)
        moneyplus = font.render("+ " + str(money_render_plus) + " $", True, FONT_COLOR69)

        money1Rect = money1.get_rect()
        money1Rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 80)
        SCREEN.blit(money1, money1Rect)

        scoreRect = score.get_rect()
        scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
        SCREEN.blit(score, scoreRect)

        moneyplusRect = moneyplus.get_rect()
        moneyplusRect.center = (SCREEN_WIDTH // 2 + 130, SCREEN_HEIGHT // 2 + 115)
        SCREEN.blit(moneyplus, moneyplusRect)


            # Draw the score on the screen.

        with open("highscore.txt", 'r') as datei:
                # Den gesamten Inhalt der Datei lesen

            inhalt = datei.read()

        if points > float(inhalt):
            with open("highscore.txt", 'w') as datei:
                datei.write(str(points))

        score = font.render("Your Highscore: " + str(inhalt), True, FONT_COLOR)


        # Render the text and position it on the screen.
        scoreRect = score.get_rect()
        scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 6)
        SCREEN.blit(score, scoreRect)
        # Draw the text on the screen.
        # Display an image representing the game character.
        SCREEN.blit(RUNNING[0], (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 140))

        restart_game_rect = restart_game.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150))
        main_screen_rect = main_screen.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 200))

        SCREEN.blit(restart_game, restart_game_rect)
        SCREEN.blit(main_screen, main_screen_rect)

        pygame.display.update()

        # Switch between the options
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % 2
                    menu_sound_effekt.play()
                elif event.key == pygame.K_UP:
                    selected = (selected - 1) % 2
                    menu_sound_effekt.play()
                elif event.key == pygame.K_RETURN:
                    if selected == 0:
                        run = False
                        main_mission1(joystick)
                    elif selected == 1:
                        ausblenden_test()
                        main_menu(joystick)
                        quit()


def main_mission2(joystick):
    # Global variables for game settings
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles, money , points_value, skin_selection

    # Set initial game state
    run = True
    clock = pygame.time.Clock()

    if skin_selection == 0:
        player = Dinosaur()
    elif skin_selection == 1:
        player = Dinosaur_Skin1_Bird()
    elif skin_selection == 2:
        player = Dinosaur_Skin2_Duck()

    obstacles = []
    cloud = Cloud()
    game_speed = GAME_SPEED
    x_pos_bg = 0
    y_pos_bg = 750
    points = 0
    font = pygame.font.Font("assets/Other/gothic_pixel.ttf", 35)
    death_count = 0
    pause = False
    money = 0

    # Function to handle scoring (currently empty)
    def score():
        global points, game_speed, points_value
        points +=  points_value
        points = round(points,1)

    def randerscore():
        global points, score, game_speed, FONT_COLOR2
        score = font.render("Score: " + str(points), True, FONT_COLOR2)
        scoreRect = score.get_rect()
        scoreRect.center = (SCREEN_WIDTH // 2 - 880, SCREEN_HEIGHT - 650)
        SCREEN.blit(score, scoreRect)
        pygame.display.update()

    # Function to handle background movement
    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            x_pos_bg = 0
        x_pos_bg -= game_speed

    # Function to unpause the game
    def unpause():
        nonlocal pause, run
        pause = False
        run = True

    # Function to pause the game
    def paused():
        nonlocal pause
        pause = True
        font = pygame.font.Font("assets/Other/gothic_pixel.ttf", 60)
        text = font.render("Game Paused, Press 'Esc' to Unpause", True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3)
        SCREEN.blit(text, textRect)
        pygame.display.update()

        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    unpause()

    # Main game loop
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                paused()

        # Fill screen with white color
        SCREEN.fill((255, 255, 255))
        # Get user input
        userInput = pygame.key.get_pressed()

        # Update and draw player and cloud

        background()

        player.draw(SCREEN)
        player.update(userInput)
        cloud.draw(SCREEN)
        cloud.update()


        # Handle obstacles
        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(BIRD))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update(obstacles)
            if player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(0)
                death_count += 1
                death_mission2()

        # Update background and score and rander score
        score()
        randerscore()
        # Update display and tick clock
        clock.tick(60)
        pygame.display.update()


def death_mission2(joystick=None):
    money_render_plus = round(money_render_plus, 2)
    run = True
    FONT_COLOR69 = (0, 255, 000)
    selected = 0  # 0 for 'Start Game', 1 for 'Quit'
    with open("money.txt", 'r') as f:
        old_money = float(f.read())

        money = old_money + points * 0.1
        money = round(money, 2)
        money_render_plus = points * 0.1
        money_render_plus = round(money_render_plus,2)
        with open("money.txt", 'w') as f:
            f.write(str(money))

    while run:

        font = pygame.font.Font("assets/Other/gothic_pixel.ttf", 45)  # Set the font and size for the text.
        pygame.display.update()  # Update the entire screen with everything drawn.

        # Options text
        if selected == 0:

            restart_game = font.render("Retry <-", True, FONT_COLOR)
            main_screen = font.render("Back to Main Menu", True, FONT_COLOR)
            SCREEN.fill((128, 128, 128))

        else:

            restart_game = font.render("Retry", True, FONT_COLOR)
            main_screen = font.render("Back to Main Menu<-", True, FONT_COLOR)
            SCREEN.fill((128, 128, 128))



        score = font.render("Your Score: " + str(points), True, FONT_COLOR)
        money1 = font.render("Your Money: " + str(money), True, FONT_COLOR)
        moneyplus = font.render("+ " + str(money_render_plus) + " $", True, FONT_COLOR69)

        money1Rect = money1.get_rect()
        money1Rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 80)
        SCREEN.blit(money1, money1Rect)

        scoreRect = score.get_rect()
        scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
        SCREEN.blit(score, scoreRect)

        moneyplusRect = moneyplus.get_rect()
        moneyplusRect.center = (SCREEN_WIDTH // 2 + 130, SCREEN_HEIGHT // 2 + 115)
        SCREEN.blit(moneyplus, moneyplusRect)


            # Draw the score on the screen.

        with open("highscore.txt", 'r') as datei:
                # Den gesamten Inhalt der Datei lesen

            inhalt = datei.read()

        if points > float(inhalt):
            with open("highscore.txt", 'w') as datei:
                datei.write(str(points))

        score = font.render("Your Highscore: " + str(inhalt), True, FONT_COLOR)


        # Render the text and position it on the screen.
        scoreRect = score.get_rect()
        scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 6)
        SCREEN.blit(score, scoreRect)
        # Draw the text on the screen.
        # Display an image representing the game character.
        SCREEN.blit(RUNNING[0], (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 140))

        restart_game_rect = restart_game.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150))
        main_screen_rect = main_screen.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 200))

        SCREEN.blit(restart_game, restart_game_rect)
        SCREEN.blit(main_screen, main_screen_rect)

        pygame.display.update()

        # Switch between the options
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % 2
                    menu_sound_effekt.play()
                elif event.key == pygame.K_UP:
                    selected = (selected - 1) % 2
                    menu_sound_effekt.play()
                elif event.key == pygame.K_RETURN:
                    if selected == 0:
                        run = False
                        main_mission2(joystick)
                    elif selected == 1:
                        ausblenden_test()
                        main_menu(joystick)
                        quit()


def main_mission3(joystick=None):
    # Global variables for game settings
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles, money , points_value, skin_selection

    # Set initial game state
    run = True
    clock = pygame.time.Clock()

    if skin_selection == 0:
        player = Dinosaur()
    elif skin_selection == 1:
        player = Dinosaur_Skin1_Bird()
    elif skin_selection == 2:
        player = Dinosaur_Skin2_Duck()

    obstacles = []
    cloud = Cloud()
    game_speed = GAME_SPEED
    x_pos_bg = 0
    y_pos_bg = 750
    points = 0
    font = pygame.font.Font("assets/Other/gothic_pixel.ttf", 35)
    death_count = 0
    pause = False
    money = 0

    # Function to handle scoring (currently empty)
    def score():
        global points, game_speed, points_value
        points +=  points_value
        points = round(points,1)

    def randerscore():
        global points, score, game_speed, FONT_COLOR2
        score = font.render("Score: " + str(points), True, FONT_COLOR2)
        scoreRect = score.get_rect()
        scoreRect.center = (SCREEN_WIDTH // 2 - 880, SCREEN_HEIGHT - 650)
        SCREEN.blit(score, scoreRect)
        pygame.display.update()

    # Function to handle background movement
    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            x_pos_bg = 0
        x_pos_bg -= game_speed

    # Function to unpause the game
    def unpause():
        nonlocal pause, run
        pause = False
        run = True

    # Function to pause the game
    def paused():
        nonlocal pause
        pause = True
        font = pygame.font.Font("assets/Other/gothic_pixel.ttf", 60)
        text = font.render("Game Paused, Press 'Esc' to Unpause", True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3)
        SCREEN.blit(text, textRect)
        pygame.display.update()

        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    unpause()

    # Main game loop
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                paused()

        # Fill screen with white color
        SCREEN.fill((255, 255, 255))
        # Get user input
        userInput = pygame.key.get_pressed()

        # Update and draw player and cloud

        background()

        player.draw(SCREEN)
        player.update(userInput)
        cloud.draw(SCREEN)
        cloud.update()


        # Handle obstacles
        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(BIRD))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update(obstacles)
            if player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(0)
                death_count += 1
                death_mission3()

        # Update background and score and rander score
        score()
        randerscore()
        # Update display and tick clock
        clock.tick(60)
        pygame.display.update()


def death_mission3(joystick=None):
    money_render_plus = round(money_render_plus, 2)
    run = True
    FONT_COLOR69 = (0, 255, 000)
    selected = 0  # 0 for 'Start Game', 1 for 'Quit'
    with open("money.txt", 'r') as f:
        old_money = float(f.read())

        money = old_money + points * 0.1
        money = round(money, 2)
        money_render_plus = points * 0.1
        money_render_plus = round(money_render_plus,2)
        with open("money.txt", 'w') as f:
            f.write(str(money))

    while run:

        font = pygame.font.Font("assets/Other/gothic_pixel.ttf", 55)  # Set the font and size for the text.
        pygame.display.update()  # Update the entire screen with everything drawn.

        # Options text
        if selected == 0:

            restart_game = font.render("Retry <-", True, FONT_COLOR)
            main_screen = font.render("Back to Main Menu", True, FONT_COLOR)
            SCREEN.fill((128, 128, 128))

        else:

            restart_game = font.render("Retry", True, FONT_COLOR)
            main_screen = font.render("Back to Main Menu<-", True, FONT_COLOR)
            SCREEN.fill((128, 128, 128))



        score = font.render("Your Score: " + str(points), True, FONT_COLOR)
        money1 = font.render("Your Money: " + str(money), True, FONT_COLOR)
        moneyplus = font.render("+ " + str(money_render_plus) + " $", True, FONT_COLOR69)

        money1Rect = money1.get_rect()
        money1Rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 80)
        SCREEN.blit(money1, money1Rect)

        scoreRect = score.get_rect()
        scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
        SCREEN.blit(score, scoreRect)

        moneyplusRect = moneyplus.get_rect()
        moneyplusRect.center = (SCREEN_WIDTH // 2 + 130, SCREEN_HEIGHT // 2 + 115)
        SCREEN.blit(moneyplus, moneyplusRect)


            # Draw the score on the screen.

        with open("highscore.txt", 'r') as datei:
                # Den gesamten Inhalt der Datei lesen

            inhalt = datei.read()

        if points > float(inhalt):
            with open("highscore.txt", 'w') as datei:
                datei.write(str(points))

        score = font.render("Your Highscore: " + str(inhalt), True, FONT_COLOR)


        # Render the text and position it on the screen.
        scoreRect = score.get_rect()
        scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 6)
        SCREEN.blit(score, scoreRect)
        # Draw the text on the screen.
        # Display an image representing the game character.
        SCREEN.blit(RUNNING[0], (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 140))

        restart_game_rect = restart_game.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150))
        main_screen_rect = main_screen.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 200))

        SCREEN.blit(restart_game, restart_game_rect)
        SCREEN.blit(main_screen, main_screen_rect)

        pygame.display.update()

        # Switch between the options
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % 2
                    menu_sound_effekt.play()
                elif event.key == pygame.K_UP:
                    selected = (selected - 1) % 2
                    menu_sound_effekt.play()
                elif event.key == pygame.K_RETURN:
                    if selected == 0:
                        run = False
                        main_mission3(joystick)
                    elif selected == 1:
                        ausblenden_test()
                        main_menu(joystick)
                        quit()



skin_selection_player2 = 0

with open("skinselectionplayer2.txt", 'r') as f:
    skin_selection_player2 = int(f.read())


def main_Coop(joystick=None):
    # Global variables for game settings
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles, money , points_value, skin_selection, skin_selection_player2

    # Set initial game state
    run = True
    clock = pygame.time.Clock()

    if skin_selection == 0:
        player = Dinosaur()
    elif skin_selection == 1:
        player = Dinosaur_Skin1_Bird()
    elif skin_selection == 2:
        player = Dinosaur_Skin2_Duck()

    if skin_selection_player2 == 0:
        player2 = Dinosaur_player2()
    elif skin_selection_player2 == 1:
        player2 = Bird_player2()
    elif skin_selection_player2 == 2:
        player2 = Duck_player2()


    obstacles = []
    cloud = Cloud()
    game_speed = GAME_SPEED
    x_pos_bg = 0
    y_pos_bg = 750
    points = 0
    font = pygame.font.Font("assets/Other/gothic_pixel.ttf", 35)
    font2 = pygame.font.Font("assets/Other/gothic_pixel.ttf", 65)
    death_count = 0
    pause = False
    money = 0
    respawntime = 500
    death_count2 = 0
    points_value = 0.1
    respawntimer = 500
    # Function to handle scoring (currently empty)
    def score():
        global points, game_speed, points_value
        points +=  points_value
        points = round(points,1)

    def randerscore():
        global points, score, game_speed, FONT_COLOR2
        score = font.render("Score: " + str(points), True, FONT_COLOR2)
        scoreRect = score.get_rect()
        scoreRect.midleft = (10, SCREEN_HEIGHT - 650)
        SCREEN.blit(score, scoreRect)
        pygame.display.update()

    def randerrespawntimer():
        global points, score, game_speed, FONT_COLOR2
        respawntimetext = font2.render("Time until Respawn: " + str(respawntime), True, FONT_COLOR2)
        respawntimetextRect = respawntimetext.get_rect()
        respawntimetextRect.center = (SCREEN_WIDTH // 2 , SCREEN_HEIGHT - 850)
        SCREEN.blit(respawntimetext, respawntimetextRect)


    # Function to handle background movement
    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            x_pos_bg = 0
        x_pos_bg -= game_speed

    # Function to unpause the game
    def unpause():
        nonlocal pause, run
        pause = False
        run = True

    # Function to pause the game
    def paused():
        nonlocal pause
        pause = True
        font = pygame.font.Font("freesansbold.ttf", 30)
        text = font.render("Game Paused, Press 'Esc' to Unpause", True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3)
        SCREEN.blit(text, textRect)
        pygame.display.update()

        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    unpause()

    # Main game loop
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                paused()

        # Fill screen with white color
        SCREEN.fill((255, 255, 255))
        # Get user input
        userInput = pygame.key.get_pressed()

        # Update and draw player and cloud

        background()
        if death_count <= 0:
            player.draw(SCREEN)
            player.update(userInput)
        if death_count2 <= 0:
            player2.draw(SCREEN)
            player2.update(userInput)

        cloud.draw(SCREEN)
        cloud.update()

        if death_count > 0:
            respawntime = respawntime - 1
            randerrespawntimer()
        if death_count2 > 0:
            respawntime = respawntime - 1
            randerrespawntimer()

        if respawntime == 0:
            obstacles = []
            death_count = 0
            death_count2 = 0
            respawntime = respawntimer + 150
            respawntimer = respawntime

        if respawntime == 0:
            obstacles = []
            death_count2 = 0
            respawntime = respawntimer + 150
            respawntimer = respawntime

        # Handle obstacles
        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(BIRD))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update(obstacles)
            if player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(0)
                death_count += 1
            if player2.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(0)
                death_count2 += 1
        if death_count >=1 and death_count2 >= 1:
            death_screen_restart_select_coop(money_render_plus)


        # Update background and score and rander score
        score()
        randerscore()
        # Update display and tick clock
        clock.tick(60)
        pygame.display.update()





def main_Wettkampf(joystick=None):
    # Global variables for game settings
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles, money , points_value, skin_selection, skin_selection_player2, points2, death_count, death_count2

    # Set initial game state
    run = True
    clock = pygame.time.Clock()

    if skin_selection == 0:
        player = Dinosaur()
    elif skin_selection == 1:
        player = Dinosaur_Skin1_Bird()
    elif skin_selection == 2:
        player = Dinosaur_Skin2_Duck()

    if skin_selection_player2 == 0:
        player2 = Dinosaur_player2()
    elif skin_selection_player2 == 1:
        player2 = Bird_player2()
    elif skin_selection_player2 == 2:
        player2 = Duck_player2()


    obstacles = []
    cloud = Cloud()
    game_speed = GAME_SPEED
    x_pos_bg = 0
    y_pos_bg = 750
    points = 0
    points2 = 0
    font = pygame.font.Font("assets/Other/gothic_pixel.ttf", 35)
    death_count = 3
    death_count2 = 3
    pause = False
    money = 0
    points_value = 0.1

    # Function to handle scoring (currently empty)
    def score():
        global points, game_speed, points_value
        points +=  points_value
        points = round(points,1)

    def score2():
        global points2, game_speed, points_value
        points2 +=  points_value
        points2 = round(points2,1)



    def randerscore():
        global points, score, game_speed, FONT_COLOR2, points2, score, game_speed, FONT_COLOR2, death_count, death_count2
        score = font.render("Player1 Score: " + str(points), True, FONT_COLOR2)
        scoreRect = score.get_rect()
        scoreRect.midleft = (10, SCREEN_HEIGHT - 750)
        SCREEN.blit(score, scoreRect)


        score2 = font.render("Player2 Score: " + str(points2), True, FONT_COLOR2)
        score2Rect = score.get_rect()
        score2Rect.midleft = (10, SCREEN_HEIGHT - 700)
        SCREEN.blit(score2, score2Rect)

        health1 = font.render("Health: " + str(death_count), True, FONT_COLOR2)
        health1Rect = health1.get_rect()
        health1Rect.midleft = (550, SCREEN_HEIGHT - 750)
        SCREEN.blit(health1, health1Rect)

        health2 = font.render("Health: " + str(death_count2), True, FONT_COLOR2)
        health2Rect = health2.get_rect()
        health2Rect.midleft = (550 , SCREEN_HEIGHT - 700)
        SCREEN.blit(health2, health2Rect)
        pygame.display.update()

    # Function to handle background movement
    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            x_pos_bg = 0
        x_pos_bg -= game_speed

    # Function to unpause the game
    def unpause():
        nonlocal pause, run
        pause = False
        run = True

    # Function to pause the game
    def paused():
        nonlocal pause
        pause = True
        font = pygame.font.Font("assets/Other/gothic_pixel.ttf", 60)
        text = font.render("Game Paused, Press 'Esc' to Unpause", True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3)
        SCREEN.blit(text, textRect)
        pygame.display.update()

        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    unpause()

    # Main game loop
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                paused()

        # Fill screen with white color
        SCREEN.fill((255, 255, 255))
        # Get user input
        userInput = pygame.key.get_pressed()

        # Update and draw player and cloud

        background()
        player.draw(SCREEN)
        player.update(userInput)
        player2.draw(SCREEN)
        player2.update(userInput)
        cloud.draw(SCREEN)
        cloud.update()


        # Handle obstacles
        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(BIRD))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update(obstacles)
            if player.dino_rect.colliderect(obstacle.rect):
                death_count -= 1
                points -= 10
                obstacles = []
                if death_count == 0:
                    menutotwettkampf(death_count)
            if player2.dino_rect.colliderect(obstacle.rect):
                death_count2 -= 1
                obstacles=[]
                points2 -= 10
                if death_count2 == 0:
                    menutotwettkampf2(death_count2)


        # Update background and score and rander score
        score()
        score2()
        randerscore()
        # Update display and tick clock
        clock.tick(60)
        pygame.display.update()


def menutotwettkampf(death_count):
    global points  # Access the global points variable to display the score.
    global FONT_COLOR  # Access the global font color variable for consistent text color.
    global FONT_COLOR2
    global money
    global money1
    run = True  # Flag to keep the menu loop running.
    count = 0

    while run:
        FONT_COLOR = (255, 255, 255)  # Set the font color to white for visibility.
        FONT_COLOR2 = (000, 000, 000)
        pygame.font.init()  # Initialize Pygame font module.
        # Check if it's the start of the game or a restart after death.

        if death_count == 0:
            # Display a message to restart the game and the last score.

            death_screen_restart_select_wettkampf()


        # Event loop to handle window closing and key presses.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Quit the game if the window close button is clicked.
                run = False
                pygame.display.quit()
                pygame.quit()
                exit()

def menutotwettkampf2(death_count2):
    global points  # Access the global points variable to display the score.
    global FONT_COLOR  # Access the global font color variable for consistent text color.
    global FONT_COLOR2
    global money
    global money1
    run = True  # Flag to keep the menu loop running.
    count = 0

    while run:
        FONT_COLOR = (255, 255, 255)  # Set the font color to white for visibility.
        FONT_COLOR2 = (000, 000, 000)
        pygame.font.init()  # Initialize Pygame font module.
        # Check if it's the start of the game or a restart after death.

        death_screen_restart_select_wettkampf()


        # Event loop to handle window closing and key presses.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Quit the game if the window close button is clicked.
                run = False
                pygame.display.quit()
                pygame.quit()
                exit()



def menu(death_count):
    global points  # Access the global points variable to display the score.
    global FONT_COLOR  # Access the global font color variable for consistent text color.
    global FONT_COLOR2
    global money
    global money1
    run = True  # Flag to keep the menu loop running.
    count = 0

    money_render_plus = 0

    while run:
        FONT_COLOR = (255, 255, 255)  # Set the font color to white for visibility.
        FONT_COLOR2 = (000, 000, 000)
        pygame.font.init()  # Initialize Pygame font module.
        # Check if it's the start of the game or a restart after death.
        if death_count == 0:
            main_menu()

        elif death_count > 0:
            # Display a message to restart the game and the last score.
            if count < 1:
                SCREEN.fill((128, 128, 128))
                old_money = 0
                with open("money.txt", 'r') as f:
                    old_money = float(f.read())

                money = old_money + points * 0.1
                money = round(money,2)

                money_render_plus = points * 0.1
                round(money_render_plus, 2)

                with open("money.txt", 'w') as f:
                    f.write(str(money))
                count += 1

        death_screen_restart_select_singleplayer(money_render_plus)


        # Event loop to handle window closing and key presses.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Quit the game if the window close button is clicked.
                run = False
                pygame.display.quit()
                pygame.quit()
                exit()

def menucoop(death_count,joystick=None):
    global points  # Access the global points variable to display the score.
    global FONT_COLOR  # Access the global font color variable for consistent text color.
    global FONT_COLOR2
    global money
    global money1
    run = True  # Flag to keep the menu loop running.
    count = 0

    while run:
        FONT_COLOR = (255, 255, 255)  # Set the font color to white for visibility.
        FONT_COLOR2 = (000, 000, 000)
        pygame.font.init()  # Initialize Pygame font module.
        # Check if it's the start of the game or a restart after death.
        if death_count == 0:
            main_menu()

        elif death_count > 0:
            # Display a message to restart the game and the last score.
            if count < 1:
                SCREEN.fill((128, 128, 128))
                old_money = 0
                with open("money.txt", 'r') as f:
                    old_money = float(f.read())
                money = old_money + points * 0.1
                money_render_plus = points * 0.1
                money = round(money, 2)
                money_render_plus = round(money_render_plus, 2)
                with open("money.txt", 'w') as f:
                    f.write(str(money))
                count += 1


        # Event loop to handle window closing and key presses.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Quit the game if the window close button is clicked.
                run = False
                pygame.display.quit()
                pygame.quit()
                exit()


dinoshopselected = Dino_Shop_Icon_Selected()
dinoshopunselected = Dino_Shop_Icon_Unselected()
obstacleselected = Obstacle_Shop_Icon_Selected()
obstacleunselected = Obstacle_Shop_Icon_Unselected()
birdshopiconselected = Bird_Shop_Icon_Selected()
birdshopiconunseleted = Bird_Shop_Icon_Unselected()
trackshopselected = Track_Shop_Icon_Selected()
trackshopunselected = Track_Shop_Icon_Unselected()
powerupselected = Power_Up_Shop_Icon_Selected()
powerupunselected = Power_Up_Shop_Icon_Unselected()

blankshopselected = Blank_Shop_Icon_Selected()
blankshopunselected = Blank_Shop_Icon_Unselected()
statsstatic = Stats_Shop_Icon_Static()
buybuttonunselected = Buy_Button_Shop_Icon_Unselected()
buybuttonselected = Buy_Button_Shop_Icon_Selected()
buybuttonpressed = Buy_Button_Shop_Icon_Pressed()

dino1shopiconselected = Dino1_Shop_Icon_Selected()
dino1shopiconunselected = Dino1_Shop_Icon_Unselected()
dino2shopiconselected = Dino2_Shop_Icon_Selected()
dino2shopiconunselected = Dino2_Shop_Icon_Unselected()
dino3shopiconselected = Dino3_Shop_Icon_Selected()
dino3shopiconunselected = Dino3_Shop_Icon_Unselected()
dino4shopiconselected = Dino4_Shop_Icon_Selected()
dino4shopiconunselected = Dino4_Shop_Icon_Unselected()
dino5shopiconselected = Dino5_Shop_Icon_Selected()
dino5shopiconunselected = Dino5_Shop_Icon_Unselected()

obstacle1shopiconselected = Obstacle1_Shop_Icon_Selected()
obstacle1shopiconunselected = Obstacle1_Shop_Icon_Unselected()
obstacle2shopiconselected = Obstacle2_Shop_Icon_Selected()
obstacle2shopiconunselected = Obstacle2_Shop_Icon_Unselected()
obstacle3shopiconselected = Obstacle3_Shop_Icon_Selected()
obstacle3shopiconunselected = Obstacle3_Shop_Icon_Unselected()
obstacle4shopiconselected = Obstacle4_Shop_Icon_Selected()
obstacle4shopiconunselected = Obstacle4_Shop_Icon_Unselected()
obstacle5shopiconselected = Obstacle5_Shop_Icon_Selected()
obstacle5shopiconunselected = Obstacle5_Shop_Icon_Unselected()

bird1shopiconselected = Bird1_Shop_Icon_Selected()
bird1shopiconunselected = Bird1_Shop_Icon_Unselected()
bird2shopiconselected = Bird2_Shop_Icon_Selected()
bird2shopiconunselected = Bird2_Shop_Icon_Unselected()
bird3shopiconselected = Bird3_Shop_Icon_Selected()
bird3shopiconunselected = Bird3_Shop_Icon_Unselected()
bird4shopiconselected = Bird4_Shop_Icon_Selected()
bird4shopiconunselected = Bird4_Shop_Icon_Unselected()
bird5shopiconselected = Bird5_Shop_Icon_Selected()
bird5shopiconunselected = Bird5_Shop_Icon_Unselected()

track1shopiconselected = Track1_Shop_Icon_Selected()
track1shopiconunselected = Track1_Shop_Icon_Unselected()
track2shopiconselected = Track2_Shop_Icon_Selected()
track2shopiconunselected = Track2_Shop_Icon_Unselected()
track3shopiconselected = Track3_Shop_Icon_Selected()
track3shopiconunselected = Track3_Shop_Icon_Unselected()
track4shopiconselected = Track4_Shop_Icon_Selected()
track4shopiconunselected = Track4_Shop_Icon_Unselected()
track5shopiconselected = Track5_Shop_Icon_Selected()
track5shopiconunselected = Track5_Shop_Icon_Unselected()


powerup1shopiconselected = Powerup1_Shop_Icon_Selected()
powerup1shopiconunselected = Powerup1_Shop_Icon_Unselected()
powerup2shopiconselected = Powerup2_Shop_Icon_Selected()
powerup2shopiconunselected = Powerup2_Shop_Icon_Unselected()
powerup3shopiconselected = Powerup3_Shop_Icon_Selected()
powerup3shopiconunselected = Powerup3_Shop_Icon_Unselected()
powerup4shopiconselected = Powerup4_Shop_Icon_Selected()
powerup4shopiconunselected = Powerup4_Shop_Icon_Unselected()
powerup5shopiconselected = Powerup5_Shop_Icon_Selected()
powerup5shopiconunselected = Powerup5_Shop_Icon_Unselected()
shopselected = 0


def buy_pressed():
    buybuttonpressed.draw(SCREEN)
    pygame.display.update()


def shop_screen(joystick=None):
    global shopselected


    run = True

    while run:
        bgmainmenue.draw(SCREEN)  # Black background for the menu


        # Options text
        if shopselected == 0:

            dinoshopselected.draw(SCREEN)
            obstacleunselected.draw(SCREEN)
            birdshopiconunseleted.draw(SCREEN)
            trackshopunselected.draw(SCREEN)
            powerupunselected.draw(SCREEN)

            dino1shopiconunselected.draw(SCREEN)
            dino2shopiconunselected.draw(SCREEN)
            dino3shopiconunselected.draw(SCREEN)
            dino4shopiconunselected.draw(SCREEN)
            dino5shopiconunselected.draw(SCREEN)

            statsstatic.draw(SCREEN)
            buybuttonunselected.draw(SCREEN)
            render_money_shop()

        if shopselected == 1:
            dinoshopunselected.draw(SCREEN)
            obstacleselected.draw(SCREEN)
            birdshopiconunseleted.draw(SCREEN)
            trackshopunselected.draw(SCREEN)
            powerupunselected.draw(SCREEN)

            obstacle1shopiconunselected.draw(SCREEN)
            obstacle2shopiconunselected.draw(SCREEN)
            obstacle3shopiconunselected.draw(SCREEN)
            obstacle4shopiconunselected.draw(SCREEN)
            obstacle5shopiconunselected.draw(SCREEN)

            statsstatic.draw(SCREEN)
            buybuttonunselected.draw(SCREEN)
            render_money_shop()

        if shopselected == 2:
            dinoshopunselected.draw(SCREEN)
            obstacleunselected.draw(SCREEN)
            birdshopiconselected.draw(SCREEN)
            trackshopunselected.draw(SCREEN)
            powerupunselected.draw(SCREEN)

            bird1shopiconunselected.draw(SCREEN)
            bird2shopiconunselected.draw(SCREEN)
            bird3shopiconunselected.draw(SCREEN)
            bird4shopiconunselected.draw(SCREEN)
            bird5shopiconunselected.draw(SCREEN)


            statsstatic.draw(SCREEN)
            buybuttonunselected.draw(SCREEN)
            render_money_shop()


        if shopselected == 3:
            dinoshopunselected.draw(SCREEN)
            obstacleunselected.draw(SCREEN)
            birdshopiconunseleted.draw(SCREEN)
            trackshopselected.draw(SCREEN)
            powerupunselected.draw(SCREEN)

            track1shopiconunselected.draw(SCREEN)
            track2shopiconunselected.draw(SCREEN)
            track3shopiconunselected.draw(SCREEN)
            track4shopiconunselected.draw(SCREEN)
            track5shopiconunselected.draw(SCREEN)

            statsstatic.draw(SCREEN)
            buybuttonunselected.draw(SCREEN)
            render_money_shop()

        if shopselected == 4:
            dinoshopunselected.draw(SCREEN)
            obstacleunselected.draw(SCREEN)
            birdshopiconunseleted.draw(SCREEN)
            trackshopunselected.draw(SCREEN)
            powerupselected.draw(SCREEN)

            powerup1shopiconunselected.draw(SCREEN)
            powerup2shopiconunselected.draw(SCREEN)
            powerup3shopiconunselected.draw(SCREEN)
            powerup4shopiconunselected.draw(SCREEN)
            powerup5shopiconunselected.draw(SCREEN)


            statsstatic.draw(SCREEN)
            buybuttonunselected.draw(SCREEN)
            render_money_shop()

        pygame.display.update()

        # Switch between the options
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    shopselected = (shopselected + 1) % 5
                    menu_sound_effekt.play()
                elif event.key == pygame.K_LEFT:
                    shopselected = (shopselected - 1) % 5
                    menu_sound_effekt.play()
                elif event.key == pygame.K_BACKSPACE:
                    ausblenden_test()
                    main_menu()
                elif event.key == pygame.K_DOWN:
                    menu_sound_effekt.play()
                    if shopselected == 0:
                        Dino_shop_screen(joystick)
                        run = False
                    elif shopselected == 1:
                        Obstacle_shop_screen(joystick)
                        quit()
                    elif shopselected == 2:
                        Bird_shop_screen(joystick)
                        quit()
                    elif shopselected == 3:
                        Track_shop_screen(joystick)
                        quit()
                    elif shopselected == 4:
                        Powerup_shop_screen(joystick)
                        quit()



def Dino_shop_screen(joystick=None):
    global skin_selection

    run = True
    selected = 0  # 0 for 'Start Game', 1 for 'Quit'

    while run:

        # Options text
        if selected == 0:
            statsstatic.draw(SCREEN)
            dino1shopiconselected.draw(SCREEN)
            dino2shopiconunselected.draw(SCREEN)
            dino3shopiconunselected.draw(SCREEN)
            dino4shopiconunselected.draw(SCREEN)
            dino5shopiconunselected.draw(SCREEN)
            buybuttonselected.draw(SCREEN)
            render_dino_skin_duck_cost_shop()
            render_money_shop()


        if selected == 1:
            statsstatic.draw(SCREEN)
            dino1shopiconunselected.draw(SCREEN)
            dino2shopiconselected.draw(SCREEN)
            dino3shopiconunselected.draw(SCREEN)
            dino4shopiconunselected.draw(SCREEN)
            dino5shopiconunselected.draw(SCREEN)
            buybuttonselected.draw(SCREEN)
            render_money_shop()
            render_dino_skin_bird_cost_shop()

        if selected == 2:
            statsstatic.draw(SCREEN)
            dino1shopiconunselected.draw(SCREEN)
            dino2shopiconunselected.draw(SCREEN)
            dino3shopiconselected.draw(SCREEN)
            dino4shopiconunselected.draw(SCREEN)
            dino5shopiconunselected.draw(SCREEN)
            render_money_shop()
            buybuttonselected.draw(SCREEN)
            render_dino_skin3_cost_shop()

        if selected == 3:

            statsstatic.draw(SCREEN)
            dino1shopiconunselected.draw(SCREEN)
            dino2shopiconunselected.draw(SCREEN)
            dino3shopiconunselected.draw(SCREEN)
            dino4shopiconselected.draw(SCREEN)
            dino5shopiconunselected.draw(SCREEN)
            render_money_shop()
            buybuttonselected.draw(SCREEN)
            render_dino_skin4_cost_shop()


        if selected == 4:
            statsstatic.draw(SCREEN)
            dino1shopiconunselected.draw(SCREEN)
            dino2shopiconunselected.draw(SCREEN)
            dino3shopiconunselected.draw(SCREEN)
            dino4shopiconunselected.draw(SCREEN)
            dino5shopiconselected.draw(SCREEN)
            render_money_shop()
            buybuttonselected.draw(SCREEN)
            render_dino_skin5_cost_shop()


        pygame.display.update()
        last_value = 0
        # Switch between the options
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    selected = (selected + 1) % 5
                    menu_sound_effekt.play()
                elif event.key == pygame.K_LEFT:
                    selected = (selected - 1) % 5
                    menu_sound_effekt.play()
                elif event.key == pygame.K_BACKSPACE:
                    ausblenden_test()
                    main_menu(joystick)
                elif event.key == pygame.K_UP:
                    menu_sound_effekt.play()
                    shop_screen(joystick)
                elif event.key == pygame.K_RETURN:
                    buy_pressed()
                    if selected == 0:
                        with open("skin_selection.txt", 'r') as f:
                            skin_selection = float(f.read())
                        if skin_selection != 2:
                            with open("money.txt", 'r') as f:
                                old_money = float(f.read())
                            if old_money >= 300:
                                with open("skin_selection.txt", 'w') as f:
                                    skin_selection = 2
                                    f.write(str(skin_selection))
                                    round(old_money,2)
                                    with open("money.txt", 'w') as f:
                                        old_money = old_money - 300
                                        f.write(str(old_money))
                                    statsstatic.draw(SCREEN)
                                    render_money_shop()


                    elif selected == 1:
                        with open("skin_selection.txt", 'r') as f:
                            skin_selection = float(f.read())
                            if skin_selection != 1:
                                with open("money.txt", 'r') as f:
                                    old_money = float(f.read())
                                if old_money >= 500:
                                    with open("skin_selection.txt", 'w') as f:
                                        skin_selection = 1
                                        f.write(str(skin_selection))
                                        round(old_money,2)
                                        with open("money.txt", 'w') as f:
                                            old_money = old_money - 500
                                            f.write(str(old_money))
                                        statsstatic.draw(SCREEN)
                                        render_money_shop()
                    elif selected == 2:
                        with open("skin_selection.txt", 'w') as f:
                            skin_selection = 0
                            f.write(str(skin_selection))
                    elif selected == 3:
                        with open("skin_selection.txt", 'w') as f:
                            skin_selection = 0
                            f.write(str(skin_selection))
                    elif selected == 4:
                        with open("skin_selection.txt", 'w') as f:
                            skin_selection = 0
                            f.write(str(skin_selection))



def Obstacle_shop_screen(joystick=None):
    global skin_selection

    run = True
    selected = 0  # 0 for 'Start Game', 1 for 'Quit'

    while run:

        # Options text
        if selected == 0:

            obstacle1shopiconselected.draw(SCREEN)
            obstacle2shopiconunselected.draw(SCREEN)
            obstacle3shopiconunselected.draw(SCREEN)
            obstacle4shopiconunselected.draw(SCREEN)
            obstacle5shopiconunselected.draw(SCREEN)

            buybuttonselected.draw(SCREEN)

        if selected == 1:

            obstacle1shopiconunselected.draw(SCREEN)
            obstacle2shopiconselected.draw(SCREEN)
            obstacle3shopiconunselected.draw(SCREEN)
            obstacle4shopiconunselected.draw(SCREEN)
            obstacle5shopiconunselected.draw(SCREEN)

            buybuttonselected.draw(SCREEN)

        if selected == 2:

            obstacle1shopiconunselected.draw(SCREEN)
            obstacle2shopiconunselected.draw(SCREEN)
            obstacle3shopiconselected.draw(SCREEN)
            obstacle4shopiconunselected.draw(SCREEN)
            obstacle5shopiconunselected.draw(SCREEN)

            buybuttonselected.draw(SCREEN)

        if selected == 3:

            obstacle1shopiconunselected.draw(SCREEN)
            obstacle2shopiconunselected.draw(SCREEN)
            obstacle3shopiconunselected.draw(SCREEN)
            obstacle4shopiconselected.draw(SCREEN)
            obstacle5shopiconunselected.draw(SCREEN)
            buybuttonselected.draw(SCREEN)

        if selected == 4:

            obstacle1shopiconunselected.draw(SCREEN)
            obstacle2shopiconunselected.draw(SCREEN)
            obstacle3shopiconunselected.draw(SCREEN)
            obstacle4shopiconunselected.draw(SCREEN)
            obstacle5shopiconselected.draw(SCREEN)

            buybuttonselected.draw(SCREEN)

        pygame.display.update()


        # Switch between the options
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    selected = (selected + 1) % 5
                    menu_sound_effekt.play()
                elif event.key == pygame.K_LEFT:
                    selected = (selected - 1) % 5
                    menu_sound_effekt.play()
                elif event.key == pygame.K_BACKSPACE:
                    ausblenden_test()
                    main_menu()
                elif event.key == pygame.K_UP:
                    menu_sound_effekt.play()
                    shop_screen()
                elif event.key == pygame.K_RETURN:
                    buy_pressed()
                    if selected == 0:
                        skin_selection = 1
                        shop_screen()
                        run = False

                    elif selected == 1:
                        skin_selection = 2
                        shop_screen()
                        quit()

                    elif selected == 2:
                        skin_selection = 0
                        shop_screen()
                        quit()
                    elif selected == 3:

                        run = False
                    elif selected == 4:
                        quit()

def Bird_shop_screen(joystick=None):


    run = True
    selected = 0  # 0 for 'Start Game', 1 for 'Quit'

    while run:

        # Options text
        if selected == 0:

            bird1shopiconselected.draw(SCREEN)
            bird2shopiconunselected.draw(SCREEN)
            bird3shopiconunselected.draw(SCREEN)
            bird4shopiconunselected.draw(SCREEN)
            bird5shopiconunselected.draw(SCREEN)

            buybuttonselected.draw(SCREEN)

        if selected == 1:

            bird1shopiconunselected.draw(SCREEN)
            bird2shopiconselected.draw(SCREEN)
            bird3shopiconunselected.draw(SCREEN)
            bird4shopiconunselected.draw(SCREEN)
            bird5shopiconunselected.draw(SCREEN)

            buybuttonselected.draw(SCREEN)

        if selected == 2:

            bird1shopiconunselected.draw(SCREEN)
            bird2shopiconunselected.draw(SCREEN)
            bird3shopiconselected.draw(SCREEN)
            bird4shopiconunselected.draw(SCREEN)
            bird5shopiconunselected.draw(SCREEN)

            buybuttonselected.draw(SCREEN)

        if selected == 3:


            bird1shopiconunselected.draw(SCREEN)
            bird2shopiconunselected.draw(SCREEN)
            bird3shopiconunselected.draw(SCREEN)
            bird4shopiconselected.draw(SCREEN)
            bird5shopiconunselected.draw(SCREEN)

            buybuttonselected.draw(SCREEN)

        if selected == 4:

            bird1shopiconunselected.draw(SCREEN)
            bird2shopiconunselected.draw(SCREEN)
            bird3shopiconunselected.draw(SCREEN)
            bird4shopiconunselected.draw(SCREEN)
            bird5shopiconselected.draw(SCREEN)

            buybuttonselected.draw(SCREEN)

        pygame.display.update()

        # Switch between the options
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    selected = (selected + 1) % 5
                    menu_sound_effekt.play()
                elif event.key == pygame.K_LEFT:
                    selected = (selected - 1) % 5
                    menu_sound_effekt.play()
                elif event.key == pygame.K_BACKSPACE:
                    ausblenden_test()
                    main_menu()
                elif event.key == pygame.K_UP:
                    menu_sound_effekt.play()
                    shop_screen()
                elif event.key == pygame.K_RETURN:
                    if selected == 0:
                        run = False

                    elif selected == 1:

                        quit()
                    elif selected == 2:

                        quit()
                    elif selected == 3:

                        quit()
                    elif selected == 4:

                        quit()

def Track_shop_screen(joystick=None):


    run = True
    selected = 0  # 0 for 'Start Game', 1 for 'Quit'

    while run:

        # Options text
        if selected == 0:

            track1shopiconselected.draw(SCREEN)
            track2shopiconunselected.draw(SCREEN)
            track3shopiconunselected.draw(SCREEN)
            track4shopiconunselected.draw(SCREEN)
            track5shopiconunselected.draw(SCREEN)

            buybuttonselected.draw(SCREEN)

        if selected == 1:

            track1shopiconunselected.draw(SCREEN)
            track2shopiconselected.draw(SCREEN)
            track3shopiconunselected.draw(SCREEN)
            track4shopiconunselected.draw(SCREEN)
            track5shopiconunselected.draw(SCREEN)

            buybuttonselected.draw(SCREEN)

        if selected == 2:

            track1shopiconunselected.draw(SCREEN)
            track2shopiconunselected.draw(SCREEN)
            track3shopiconselected.draw(SCREEN)
            track4shopiconunselected.draw(SCREEN)
            track5shopiconunselected.draw(SCREEN)

            buybuttonselected.draw(SCREEN)

        if selected == 3:


            track1shopiconunselected.draw(SCREEN)
            track2shopiconunselected.draw(SCREEN)
            track3shopiconunselected.draw(SCREEN)
            track4shopiconselected.draw(SCREEN)
            track5shopiconunselected.draw(SCREEN)

            buybuttonselected.draw(SCREEN)

        if selected == 4:

            track1shopiconunselected.draw(SCREEN)
            track2shopiconunselected.draw(SCREEN)
            track3shopiconunselected.draw(SCREEN)
            track4shopiconunselected.draw(SCREEN)
            track5shopiconselected.draw(SCREEN)

            buybuttonselected.draw(SCREEN)

        pygame.display.update()

        # Switch between the options
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    selected = (selected + 1) % 5
                    menu_sound_effekt.play()
                elif event.key == pygame.K_LEFT:
                    selected = (selected - 1) % 5
                    menu_sound_effekt.play()
                elif event.key == pygame.K_BACKSPACE:
                    ausblenden_test()
                    main_menu(joystick)
                elif event.key == pygame.K_UP:
                    menu_sound_effekt.play()
                    shop_screen(joystick)
                elif event.key == pygame.K_RETURN:
                    if selected == 0:
                        run = False
                    elif selected == 1:
                        run = False
                    elif selected == 2:
                        run = False
                    elif selected == 3:
                        run = False
                    elif selected == 4:
                        run = False

def Powerup_shop_screen(joystick=None):


    run = True
    selected = 0  # 0 for 'Start Game', 1 for 'Quit'

    while run:

        # Options text
        if selected == 0:
            statsstatic.draw(SCREEN)
            powerup1shopiconselected.draw(SCREEN)
            powerup2shopiconunselected.draw(SCREEN)
            powerup3shopiconunselected.draw(SCREEN)
            powerup4shopiconunselected.draw(SCREEN)
            powerup5shopiconunselected.draw(SCREEN)
            buybuttonselected.draw(SCREEN)
            render_powerup_doublepoints_cost_shop()
            render_money_shop()


        if selected == 1:

            powerup1shopiconunselected.draw(SCREEN)
            powerup2shopiconselected.draw(SCREEN)
            powerup3shopiconunselected.draw(SCREEN)
            powerup4shopiconunselected.draw(SCREEN)
            powerup5shopiconunselected.draw(SCREEN)

            buybuttonselected.draw(SCREEN)

        if selected == 2:

            powerup1shopiconunselected.draw(SCREEN)
            powerup2shopiconunselected.draw(SCREEN)
            powerup3shopiconselected.draw(SCREEN)
            powerup4shopiconunselected.draw(SCREEN)
            powerup5shopiconunselected.draw(SCREEN)

            buybuttonselected.draw(SCREEN)

        if selected == 3:


            powerup1shopiconunselected.draw(SCREEN)
            powerup2shopiconunselected.draw(SCREEN)
            powerup3shopiconunselected.draw(SCREEN)
            powerup4shopiconselected.draw(SCREEN)
            powerup5shopiconunselected.draw(SCREEN)

            buybuttonselected.draw(SCREEN)

        if selected == 4:

            powerup1shopiconunselected.draw(SCREEN)
            powerup2shopiconunselected.draw(SCREEN)
            powerup3shopiconunselected.draw(SCREEN)
            powerup4shopiconunselected.draw(SCREEN)
            powerup5shopiconselected.draw(SCREEN)

            buybuttonselected.draw(SCREEN)

        pygame.display.update()

        # Switch between the options
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    selected = (selected + 1) % 5
                    menu_sound_effekt.play()
                elif event.key == pygame.K_LEFT:
                    selected = (selected - 1) % 5
                    menu_sound_effekt.play()
                elif event.key == pygame.K_BACKSPACE:
                    ausblenden_test()
                    main_menu(joystick)
                elif event.key == pygame.K_UP:
                    menu_sound_effekt.play()
                    shop_screen(joystick)
                elif event.key == pygame.K_RETURN:
                    buybuttonpressed.draw(SCREEN)
                    pygame.display.update()
                    if selected == 0:
                        with open("items_unlocked/double_points_unlocked.txt", 'r') as f:
                            skin_selection = float(f.read())
                        if skin_selection != 1:
                            with open("money.txt", 'r') as f:
                                old_money = float(f.read())
                            if old_money >= 85:
                                with open("items_unlocked/double_points_unlocked.txt", 'w') as f:
                                    skin_selection = 1
                                    f.write(str(skin_selection))
                                    round(old_money,2)
                                    with open("money.txt", 'w') as f:
                                        old_money = old_money - 85
                                        f.write(str(old_money))
                                    statsstatic.draw(SCREEN)
                                    render_money_shop()
                    elif selected == 1:
                        with open("items_unlocked/double_points_unlocked.txt", 'w') as f:
                            double_points_unlocked_checked = 0
                            f.write(str(double_points_unlocked_checked))
                    elif selected == 2:
                        run = False
                    elif selected == 3:
                        run = False
                    elif selected == 4:
                        run = False



def resetgame_yes_no(joystick=None):

    run = True
    selected = 0  # 0 for 'Start Game', 1 for 'Quit'

    while run:
        SCREEN.fill((0, 0, 0))  # Black background for the menu
        fontbig = pygame.font.Font("assets/Other/gothic_pixel.ttf", 120)
        font = pygame.font.Font("assets/Other/gothic_pixel.ttf", 60)
        title = fontbig.render("ARE YOU SURE?", True, FONT_COLOR)

        # Options text
        if selected == 0:
            mission_mode = font.render("Yes! <-", True, FONT_COLOR)
            chellenger_sellected.draw(SCREEN)
            singleplayer_mode = font.render("Nope", True, FONT_COLOR)
            vanillagm.draw(SCREEN)


        if selected == 1:
            mission_mode = font.render("YES!", True, FONT_COLOR)
            chellenger_unsellected.draw(SCREEN)
            singleplayer_mode = font.render("Nope <-", True, FONT_COLOR)
            vanillagm_sellected.draw(SCREEN)




        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4 - 100))
        mission_mode_rect = mission_mode.get_rect(center=(SCREEN_WIDTH // 2 - 300, SCREEN_HEIGHT //2))
        singleplayer_mode_rect = singleplayer_mode.get_rect(center=(SCREEN_WIDTH // 2 + 300, SCREEN_HEIGHT // 2))

        SCREEN.blit(title, title_rect)
        SCREEN.blit(mission_mode, mission_mode_rect)
        SCREEN.blit(singleplayer_mode, singleplayer_mode_rect)

        pygame.display.update()

        # Switch between the options
        for event in pygame.event.get():
            pygame.event.pump()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    selected = (selected + 1) % 2
                    menu_sound_effekt.play()
                elif event.key == pygame.K_LEFT:
                    selected = (selected - 1) % 2
                    menu_sound_effekt.play()
                elif event.key == pygame.K_BACKSPACE:
                    ausblenden_test()
                    settings_menu(joystick)
                elif event.key == pygame.K_RETURN:
                    if selected == 0:

                        money = 0
                        with open("money.txt", 'w') as f:
                            f.write(str(money))
                        highscore = 0
                        with open("highscore.txt", 'w') as f:
                            f.write(str(highscore))
                        skin_selection = 0
                        with open("skin_selection.txt.txt", 'w') as f:
                            f.write(str(skin_selection))
                        skin_selection_player2 = 0
                        with open("skinselectionplayer2.txt", 'w') as f:
                            f.write(str(skin_selection_player2))
                        double_points_unlocked_checked = 0
                        with open("items_unlocked/double_points_unlocked.txt", 'w') as f:
                            f.write(str(double_points_unlocked_checked))

                        settings_menu(joystick)
                        run = False
                    elif selected == 1:
                        run = False
                        settings_menu(joystick)

def render_money_shop():
    font = pygame.font.Font("assets/Other/gothic_pixel.ttf", 80)
    FONT_COLOR = (0, 0, 0)

    with open("money.txt", 'r') as f:
        moneyshop = float(f.read())
    moneyshop = round(moneyshop,2)
    money1 = font.render(str(moneyshop) + "",True, FONT_COLOR)
    money1Rect = money1.get_rect()
    money1Rect.midleft = (SCREEN_WIDTH // 2 + 580, SCREEN_HEIGHT // 2 + 365)
    SCREEN.blit(money1, money1Rect)

def render_dino_skin_duck_cost_shop():
    font = pygame.font.Font("assets/Other/gothic_pixel.ttf", 80)
    FONT_COLOR = (19, 48, 30)
    duck_cost300 = 300
    duck_cost = font.render("" + str(duck_cost300) + "",True, FONT_COLOR)
    duck_costRect = duck_cost.get_rect()
    duck_costRect.midleft = (SCREEN_WIDTH // 2 + 150, SCREEN_HEIGHT // 2 + 365)
    SCREEN.blit(duck_cost, duck_costRect)

def render_dino_skin_bird_cost_shop():
    font = pygame.font.Font("assets/Other/gothic_pixel.ttf", 80)
    FONT_COLOR = (19, 48, 30)
    duck_cost300 = 500
    duck_cost = font.render("" + str(duck_cost300) + "",True, FONT_COLOR)
    duck_costRect = duck_cost.get_rect()
    duck_costRect.midleft = (SCREEN_WIDTH // 2 + 150, SCREEN_HEIGHT // 2 + 365)
    SCREEN.blit(duck_cost, duck_costRect)

def render_dino_skin3_cost_shop():
    font = pygame.font.Font("assets/Other/gothic_pixel.ttf", 80)
    FONT_COLOR = (19, 48, 30)
    cost_cost = 0
    cost = font.render("" + str(cost_cost) + "",True, FONT_COLOR)
    costRect = cost.get_rect()
    costRect.midleft = (SCREEN_WIDTH // 2 + 150, SCREEN_HEIGHT // 2 + 365)
    SCREEN.blit(cost, costRect)


def render_dino_skin4_cost_shop():
    font = pygame.font.Font("assets/Other/gothic_pixel.ttf", 80)
    FONT_COLOR = (19, 48, 30)
    cost_cost = 0
    cost = font.render("" + str(cost_cost) + "",True, FONT_COLOR)
    costRect = cost.get_rect()
    costRect.midleft = (SCREEN_WIDTH // 2 + 150, SCREEN_HEIGHT // 2 + 365)
    SCREEN.blit(cost, costRect)



def render_dino_skin5_cost_shop():
    font = pygame.font.Font("assets/Other/gothic_pixel.ttf", 80)
    FONT_COLOR = (19, 48, 30)
    cost_cost = 0
    cost = font.render("" + str(cost_cost) + "",True, FONT_COLOR)
    costRect = cost.get_rect()
    costRect.midleft = (SCREEN_WIDTH // 2 + 150, SCREEN_HEIGHT // 2 + 365)
    SCREEN.blit(cost, costRect)

def render_powerup_doublepoints_cost_shop():
    font = pygame.font.Font("assets/Other/gothic_pixel.ttf", 80)
    FONT_COLOR = (19, 48, 30)
    cost_cost = 85
    cost = font.render("" + str(cost_cost) + "",True, FONT_COLOR)
    costRect = cost.get_rect()
    costRect.midleft = (SCREEN_WIDTH // 2 + 150, SCREEN_HEIGHT // 2 + 365)
    SCREEN.blit(cost, costRect)


def items_reading():
    global double_points_unlocked_checked
    with open("items_unlocked/double_points_unlocked.txt", 'r') as f:
        double_points_unlocked_checked = float(f.read())






t1 = threading.Thread(target=menu(death_count=0), daemon=True)
pygame.init()
t1.start()
