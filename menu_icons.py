import random
import pygame
from settings import SCREEN_WIDTH, GAME_SPEED, SCREEN_HEIGHT
from resources import VANILLA_GAMEMODE_ICON_UNSELECTED, VANILLA_GAMEMODE_ICON_SELECTED, CHALLENGER_GAMEMODE_ICON_SELECTED, CHALLENGER_GAMEMODE_ICON_UNSELECTED, MULTIPLAYER_GAMEMODE_ICON_UNSELECTED, MULTIPLAYER_GAMEMODE_ICON_SELECTED
from resources import test, DINO_SHOP_UNSELECTED, DINO_SHOP_SELECTED, BIRD_SHOP_UNSELECTED, BIRD_SHOP_SELECTED, OBSTACLE_SHOP_SELECTED, OBSTACLE_SHOP_UNSELECTED, TRACK_SHOP_SELECTED, TRACK_SHOP_UNSELECTED, POWER_UP_SHOP_UNSELECTED, POWER_UP_SHOP_SELECTED
from resources import SHOP_BLANK_SELECTED, SHOP_BLANK_UNSELECTED, SHOP_STATS_STATIC, BUY_BUTTON_UNSELECTED, BUY_BUTTON_SELECTED, BUY_BUTTON_PRESSED
from resources import SHOP_D_Skin1_SELECTED, SHOP_D_Skin1_UNSELECTED, SHOP_D_Skin2_UNSELECTED,SHOP_D_Skin2_SELECTED, SHOP_D_Skin3_UNSELECTED,SHOP_D_Skin3_SELECTED, SHOP_D_Skin4_UNSELECTED,SHOP_D_Skin4_SELECTED, SHOP_D_Skin5_UNSELECTED, SHOP_D_Skin5_SELECTED
from resources import SHOP_O_Skin1_SELECTED, SHOP_O_Skin1_UNSELECTED, SHOP_O_Skin2_UNSELECTED,SHOP_O_Skin2_SELECTED, SHOP_O_Skin3_UNSELECTED,SHOP_O_Skin3_SELECTED, SHOP_O_Skin4_UNSELECTED,SHOP_O_Skin4_SELECTED, SHOP_O_Skin5_UNSELECTED, SHOP_O_Skin5_SELECTED
from resources import SHOP_B_Skin1_SELECTED, SHOP_B_Skin1_UNSELECTED, SHOP_B_Skin2_UNSELECTED,SHOP_B_Skin2_SELECTED, SHOP_B_Skin3_UNSELECTED,SHOP_B_Skin3_SELECTED, SHOP_B_Skin4_UNSELECTED,SHOP_B_Skin4_SELECTED, SHOP_B_Skin5_UNSELECTED, SHOP_B_Skin5_SELECTED
from resources import SHOP_T_Skin1_SELECTED, SHOP_T_Skin1_UNSELECTED, SHOP_T_Skin2_UNSELECTED,SHOP_T_Skin2_SELECTED, SHOP_T_Skin3_UNSELECTED,SHOP_T_Skin3_SELECTED, SHOP_T_Skin4_UNSELECTED,SHOP_T_Skin4_SELECTED, SHOP_T_Skin5_UNSELECTED, SHOP_T_Skin5_SELECTED
from resources import SHOP_P_Skin1_SELECTED, SHOP_P_Skin1_UNSELECTED, SHOP_P_Skin2_UNSELECTED,SHOP_P_Skin2_SELECTED, SHOP_P_Skin3_UNSELECTED,SHOP_P_Skin3_SELECTED, SHOP_P_Skin4_UNSELECTED,SHOP_P_Skin4_SELECTED, SHOP_P_Skin5_UNSELECTED, SHOP_P_Skin5_SELECTED
from resources import START_GAME_SELECTED, START_GAME_UNSELECTED, SHOP_ICON_SELECTED, SHOP_ICON_UNSELECTED, QUIT_SELECTED, QUIT_UNSELECTED, INVENTORY_ICON_SELECTED, INVENTORY_ICON_UNSELECTED, BG_MAIN_MENU
from resources import SETTINGS_ICON_UNSELECTED, SETTINGS_ICON_SELECTED

from resources import BG_MAIN_MENU_1

from resources import Inventory_Blank_Unselected, Inventory_Blank_Selected

from resources import Slot_Inv_1_Unselected, Slot_Inv_1_Selected, Slot_Inv_2_Unselected, Slot_Inv_2_Selected, Slot_Inv_3_Unselected, Slot_Inv_3_Selected, Slot_Inv_4_Unselected, Slot_Inv_4_Selected, Slot_Inv_5_Unselected, Slot_Inv_5_Selected, Slot_Inv_6_Unselected, Slot_Inv_6_Selected, Slot_Inv_7_Unselected, Slot_Inv_7_Selected, Slot_Inv_8_Unselected, Slot_Inv_8_Selected, Slot_Inv_9_Unselected, Slot_Inv_9_Selected, Slot_Inv_10_Unselected, Slot_Inv_10_Selected, Slot_Inv_11_Unselected, Slot_Inv_11_Selected, Slot_Inv_12_Unselected, Slot_Inv_12_Selected, Slot_Inv_13_Unselected, Slot_Inv_13_Selected, Slot_Inv_14_Unselected, Slot_Inv_14_Selected, Slot_Inv_15_Unselected, Slot_Inv_15_Selected, Slot_Inv_16_Unselected, Slot_Inv_16_Selected, Slot_Inv_17_Unselected, Slot_Inv_17_Selected, Slot_Inv_18_Unselected, Slot_Inv_18_Selected, Slot_Inv_19_Unselected, Slot_Inv_19_Selected, Slot_Inv_20_Unselected, Slot_Inv_20_Selected, Slot_Inv_21_Unselected, Slot_Inv_21_Selected, Slot_Inv_22_Unselected, Slot_Inv_22_Selected, Slot_Inv_23_Unselected, Slot_Inv_23_Selected, Slot_Inv_24_Unselected, Slot_Inv_24_Selected
from resources import Slot_Inv_25_Unselected, Slot_Inv_25_Selected, Slot_Inv_26_Unselected, Slot_Inv_26_Selected, Slot_Inv_27_Unselected, Slot_Inv_27_Selected, Slot_Inv_28_Unselected, Slot_Inv_28_Selected, Slot_Inv_29_Unselected, Slot_Inv_29_Selected, Slot_Inv_30_Unselected, Slot_Inv_30_Selected, Slot_Inv_31_Unselected, Slot_Inv_31_Selected, Slot_Inv_32_Unselected, Slot_Inv_32_Selected, Slot_Inv_33_Unselected, Slot_Inv_33_Selected, Slot_Inv_34_Unselected, Slot_Inv_34_Selected, Slot_Inv_35_Unselected, Slot_Inv_35_Selected, Slot_Inv_36_Unselected, Slot_Inv_36_Selected

class Test:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 384
        self.y = (SCREEN_HEIGHT) // 2 - 500
        self.image = test
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))


class Inv_slot_Test_selected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 876
        self.y = (SCREEN_HEIGHT) // 2 - 280
        self.image = Inventory_Blank_Selected
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Inv_slot_Test_unselected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 876
        self.y = (SCREEN_HEIGHT) // 2 - 280
        self.image = Inventory_Blank_Unselected
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))



class Background_Main_Menu:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 960
        self.y = (SCREEN_HEIGHT) // 2 - 540
        self.image = BG_MAIN_MENU
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))



class Background_Menu_1:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 960
        self.y = (SCREEN_HEIGHT) // 2 - 540
        self.image = BG_MAIN_MENU_1
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Start_Game_Selected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 256
        self.y = (SCREEN_HEIGHT) // 2 - 100
        self.image = START_GAME_SELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))


class Start_Game_Unselected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 256
        self.y = (SCREEN_HEIGHT) // 2 - 100
        self.image = START_GAME_UNSELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Shop_Icon_Selected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 256
        self.y = (SCREEN_HEIGHT) // 2 + 100
        self.image = SHOP_ICON_SELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))


class Shop_Icon_Unselected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 256
        self.y = (SCREEN_HEIGHT) // 2 + 100
        self.image = SHOP_ICON_UNSELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Quit_Selected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 256
        self.y = (SCREEN_HEIGHT) // 2 + 300
        self.image = QUIT_SELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))


class Quit_Unselected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 256
        self.y = (SCREEN_HEIGHT) // 2 + 300
        self.image = QUIT_UNSELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))


class Inventory_Selected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 456
        self.y = (SCREEN_HEIGHT) // 2
        self.image = INVENTORY_ICON_SELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))


class Inventory_Unselected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 456
        self.y = (SCREEN_HEIGHT) // 2
        self.image = INVENTORY_ICON_UNSELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))










class Vanilla_GM:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 130
        self.y = (SCREEN_HEIGHT) // 2 - 100
        self.image = VANILLA_GAMEMODE_ICON_UNSELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Vanilla_GM_SELECTED:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 130
        self.y = (SCREEN_HEIGHT) // 2 - 100
        self.image = VANILLA_GAMEMODE_ICON_SELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Chellenger_GM_SELECTED:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 540
        self.y = (SCREEN_HEIGHT) // 2 - 100
        self.image = CHALLENGER_GAMEMODE_ICON_SELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Chellenger_GM_UNSELECTED:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 540
        self.y = (SCREEN_HEIGHT) // 2 - 100
        self.image = CHALLENGER_GAMEMODE_ICON_UNSELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))


class Multiplayer_GM_UNSELECTED:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 260
        self.y = (SCREEN_HEIGHT) // 2 - 100
        self.image = MULTIPLAYER_GAMEMODE_ICON_UNSELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Multiplayer_GM_SELECTED:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 260
        self.y = (SCREEN_HEIGHT) // 2 - 100
        self.image = MULTIPLAYER_GAMEMODE_ICON_SELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))



###Shop Icons (Kategorie)


class Dino_Shop_Icon_Selected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 960
        self.y = (SCREEN_HEIGHT) // 2 - 525
        self.image = DINO_SHOP_SELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Dino_Shop_Icon_Unselected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 960
        self.y = (SCREEN_HEIGHT) // 2 - 525
        self.image = DINO_SHOP_UNSELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Obstacle_Shop_Icon_Selected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 576
        self.y = (SCREEN_HEIGHT) // 2 - 525
        self.image = OBSTACLE_SHOP_SELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Obstacle_Shop_Icon_Unselected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 576
        self.y = (SCREEN_HEIGHT) // 2 - 525
        self.image = OBSTACLE_SHOP_UNSELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Bird_Shop_Icon_Selected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 192
        self.y = (SCREEN_HEIGHT) // 2 - 525
        self.image = BIRD_SHOP_SELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Bird_Shop_Icon_Unselected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 192
        self.y = (SCREEN_HEIGHT) // 2 - 525
        self.image = BIRD_SHOP_UNSELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Track_Shop_Icon_Selected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 192
        self.y = (SCREEN_HEIGHT) // 2 - 525
        self.image = TRACK_SHOP_SELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Track_Shop_Icon_Unselected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 192
        self.y = (SCREEN_HEIGHT) // 2 - 525
        self.image = TRACK_SHOP_UNSELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Power_Up_Shop_Icon_Selected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 576
        self.y = (SCREEN_HEIGHT) // 2 - 525
        self.image = POWER_UP_SHOP_SELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Power_Up_Shop_Icon_Unselected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 576
        self.y = (SCREEN_HEIGHT) // 2 - 525
        self.image = POWER_UP_SHOP_UNSELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

##test blank
class Blank_Shop_Icon_Selected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 576
        self.y = (SCREEN_HEIGHT) // 2 - 275
        self.image = SHOP_BLANK_SELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Blank_Shop_Icon_Unselected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 576
        self.y = (SCREEN_HEIGHT) // 2 - 275
        self.image = SHOP_BLANK_UNSELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

### Stats Test


class Stats_Shop_Icon_Static:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 960
        self.y = (SCREEN_HEIGHT) // 2 + 284
        self.image = SHOP_STATS_STATIC
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))


### Buy Button


class Buy_Button_Shop_Icon_Unselected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 640
        self.y = (SCREEN_HEIGHT) // 2 + 420
        self.image = BUY_BUTTON_UNSELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))


class Buy_Button_Shop_Icon_Selected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 640
        self.y = (SCREEN_HEIGHT) // 2 + 420
        self.image = BUY_BUTTON_SELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))


class Buy_Button_Shop_Icon_Pressed:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 640
        self.y = (SCREEN_HEIGHT) // 2 + 420
        self.image = BUY_BUTTON_PRESSED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))





###Shop Icons Skin Obstacle

class Obstacle1_Shop_Icon_Selected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 960
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_O_Skin1_SELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Obstacle1_Shop_Icon_Unselected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 960
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_O_Skin1_UNSELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))


class Obstacle2_Shop_Icon_Selected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 576
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_O_Skin2_SELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Obstacle2_Shop_Icon_Unselected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 576
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_O_Skin2_UNSELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Obstacle3_Shop_Icon_Selected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 192
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_O_Skin3_SELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Obstacle3_Shop_Icon_Unselected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 192
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_O_Skin3_UNSELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Obstacle4_Shop_Icon_Selected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 192
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_O_Skin4_SELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Obstacle4_Shop_Icon_Unselected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 192
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_O_Skin4_UNSELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Obstacle5_Shop_Icon_Selected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 576
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_O_Skin5_SELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Obstacle5_Shop_Icon_Unselected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 576
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_O_Skin5_UNSELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))


###Shop Icons Skin Dino

class Dino1_Shop_Icon_Selected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 960
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_D_Skin1_SELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Dino1_Shop_Icon_Unselected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 960
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_D_Skin1_UNSELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))


class Dino2_Shop_Icon_Selected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 576
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_D_Skin2_SELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Dino2_Shop_Icon_Unselected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 576
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_D_Skin2_UNSELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Dino3_Shop_Icon_Selected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 192
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_D_Skin3_SELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Dino3_Shop_Icon_Unselected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 192
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_D_Skin3_UNSELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Dino4_Shop_Icon_Selected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 192
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_D_Skin4_SELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Dino4_Shop_Icon_Unselected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 192
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_D_Skin4_UNSELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Dino5_Shop_Icon_Selected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 576
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_D_Skin5_SELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Dino5_Shop_Icon_Unselected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 576
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_D_Skin5_UNSELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))


###Shop Icons Skin Bird

class Bird1_Shop_Icon_Selected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 960
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_B_Skin1_SELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Bird1_Shop_Icon_Unselected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 960
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_B_Skin1_UNSELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))


class Bird2_Shop_Icon_Selected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 576
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_B_Skin2_SELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Bird2_Shop_Icon_Unselected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 576
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_B_Skin2_UNSELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Bird3_Shop_Icon_Selected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 192
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_B_Skin3_SELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Bird3_Shop_Icon_Unselected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 192
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_B_Skin3_UNSELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Bird4_Shop_Icon_Selected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 192
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_B_Skin4_SELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Bird4_Shop_Icon_Unselected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 192
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_B_Skin4_UNSELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Bird5_Shop_Icon_Selected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 576
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_B_Skin5_SELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Bird5_Shop_Icon_Unselected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 576
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_B_Skin5_UNSELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

###Shop Icons Skin Track

class Track1_Shop_Icon_Selected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 960
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_T_Skin1_SELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Track1_Shop_Icon_Unselected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 960
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_T_Skin1_UNSELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))


class Track2_Shop_Icon_Selected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 576
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_T_Skin2_SELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Track2_Shop_Icon_Unselected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 576
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_T_Skin2_UNSELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Track3_Shop_Icon_Selected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 192
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_T_Skin3_SELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Track3_Shop_Icon_Unselected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 192
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_T_Skin3_UNSELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Track4_Shop_Icon_Selected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 192
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_T_Skin4_SELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Track4_Shop_Icon_Unselected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 192
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_T_Skin4_UNSELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Track5_Shop_Icon_Selected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 576
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_T_Skin5_SELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Track5_Shop_Icon_Unselected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 576
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_T_Skin5_UNSELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))


###Shop Icons Skin Powerup

class Powerup1_Shop_Icon_Selected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 960
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_P_Skin1_SELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Powerup1_Shop_Icon_Unselected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 960
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_P_Skin1_UNSELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))


class Powerup2_Shop_Icon_Selected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 576
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_P_Skin2_SELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Powerup2_Shop_Icon_Unselected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 576
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_P_Skin2_UNSELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Powerup3_Shop_Icon_Selected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 192
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_P_Skin3_SELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Powerup3_Shop_Icon_Unselected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 192
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_P_Skin3_UNSELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Powerup4_Shop_Icon_Selected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 192
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_P_Skin4_SELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Powerup4_Shop_Icon_Unselected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 192
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_P_Skin4_UNSELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Powerup5_Shop_Icon_Selected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 576
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_P_Skin5_SELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Powerup5_Shop_Icon_Unselected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 576
        self.y = (SCREEN_HEIGHT) // 2 - 300
        self.image = SHOP_P_Skin5_UNSELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

##########################################################################
class Settings_Icon_Unselected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 470
        self.y = (SCREEN_HEIGHT) // 2 + 90
        self.image = SETTINGS_ICON_UNSELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Settings_Icon_Selected:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 - 470
        self.y = (SCREEN_HEIGHT) // 2 + 90
        self.image = SETTINGS_ICON_SELECTED
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))
######################################################################################
###Inv
class Inv_c_Slot_Selected_1:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 832 - 64
        self.y = (SCREEN_HEIGHT) // 2 - 280
        self.image = Slot_Inv_1_Selected
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Inv_c_Slot_Unselected_1:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 832 - 64
        self.y = (SCREEN_HEIGHT) // 2 - 280
        self.image = Slot_Inv_1_Unselected
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Inv_c_Slot_Selected_2:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 704 - 64
        self.y = (SCREEN_HEIGHT) // 2 - 280
        self.image = Slot_Inv_2_Selected
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Inv_c_Slot_Unselected_2:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 704 - 64
        self.y = (SCREEN_HEIGHT) // 2 - 280
        self.image = Slot_Inv_2_Unselected
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Inv_c_Slot_Selected_3:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 576 - 64
        self.y = (SCREEN_HEIGHT) // 2 - 280
        self.image = Slot_Inv_3_Selected
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Inv_c_Slot_Unselected_3:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 576 - 64
        self.y = (SCREEN_HEIGHT) // 2 - 280
        self.image = Slot_Inv_3_Unselected
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Inv_c_Slot_Selected_4:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 448 - 64
        self.y = (SCREEN_HEIGHT) // 2 - 280
        self.image = Slot_Inv_4_Selected
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Inv_c_Slot_Unselected_4:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 448 - 64
        self.y = (SCREEN_HEIGHT) // 2 - 280
        self.image = Slot_Inv_4_Unselected
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Inv_c_Slot_Selected_5:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 320 - 64
        self.y = (SCREEN_HEIGHT) // 2 - 280
        self.image = Slot_Inv_5_Selected
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Inv_c_Slot_Unselected_5:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 320 - 64
        self.y = (SCREEN_HEIGHT) // 2 - 280
        self.image = Slot_Inv_5_Unselected
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Inv_c_Slot_Selected_6:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 192 - 64
        self.y = (SCREEN_HEIGHT) // 2 - 280
        self.image = Slot_Inv_6_Selected
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Inv_c_Slot_Unselected_6:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 192 - 64
        self.y = (SCREEN_HEIGHT) // 2 - 280
        self.image = Slot_Inv_6_Unselected
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

#####
class Inv_c_Slot_Selected_7:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 832 - 64
        self.y = (SCREEN_HEIGHT) // 2 - 280 + 128
        self.image = Slot_Inv_7_Selected
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Inv_c_Slot_Unselected_7:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 832 - 64
        self.y = (SCREEN_HEIGHT) // 2 - 280 + 128
        self.image = Slot_Inv_7_Unselected
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Inv_c_Slot_Selected_8:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 704 - 64
        self.y = (SCREEN_HEIGHT) // 2 - 280 + 128
        self.image = Slot_Inv_8_Selected
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Inv_c_Slot_Unselected_8:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 704 - 64
        self.y = (SCREEN_HEIGHT) // 2 - 280 + 128
        self.image = Slot_Inv_8_Unselected
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Inv_c_Slot_Selected_9:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 576 - 64
        self.y = (SCREEN_HEIGHT) // 2 - 280 + 128
        self.image = Slot_Inv_9_Selected
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Inv_c_Slot_Unselected_9:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 576 - 64
        self.y = (SCREEN_HEIGHT) // 2 - 280 + 128
        self.image = Slot_Inv_9_Unselected
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Inv_c_Slot_Selected_10:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 448 - 64
        self.y = (SCREEN_HEIGHT) // 2 - 280 + 128
        self.image = Slot_Inv_10_Selected
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Inv_c_Slot_Unselected_10:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 448 - 64
        self.y = (SCREEN_HEIGHT) // 2 - 280 + 128
        self.image = Slot_Inv_10_Unselected
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Inv_c_Slot_Selected_11:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 320 - 64
        self.y = (SCREEN_HEIGHT) // 2 - 280 + 128
        self.image = Slot_Inv_11_Selected
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Inv_c_Slot_Unselected_11:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 320 - 64
        self.y = (SCREEN_HEIGHT) // 2 - 280 + 128
        self.image = Slot_Inv_11_Unselected
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Inv_c_Slot_Selected_12:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 192 - 64
        self.y = (SCREEN_HEIGHT) // 2 - 280 + 128
        self.image = Slot_Inv_12_Selected
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Inv_c_Slot_Unselected_12:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 192 - 64
        self.y = (SCREEN_HEIGHT) // 2 - 280 + 128
        self.image = Slot_Inv_12_Unselected
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

##############################################################################
class Inv_c_Slot_Selected_13:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 832 - 64
        self.y = (SCREEN_HEIGHT) // 2 - 280 + 256
        self.image = Slot_Inv_13_Selected
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Inv_c_Slot_Unselected_13:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 832 - 64
        self.y = (SCREEN_HEIGHT) // 2 - 280 + 256
        self.image = Slot_Inv_13_Unselected
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Inv_c_Slot_Selected_14:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 704 - 64
        self.y = (SCREEN_HEIGHT) // 2 - 280 + 256
        self.image = Slot_Inv_14_Selected
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Inv_c_Slot_Unselected_14:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 704 - 64
        self.y = (SCREEN_HEIGHT) // 2 - 280 + 256
        self.image = Slot_Inv_14_Unselected
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Inv_c_Slot_Selected_15:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 576 - 64
        self.y = (SCREEN_HEIGHT) // 2 - 280 + 256
        self.image = Slot_Inv_15_Selected
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Inv_c_Slot_Unselected_15:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 576 - 64
        self.y = (SCREEN_HEIGHT) // 2 - 280 + 256
        self.image = Slot_Inv_15_Unselected
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Inv_c_Slot_Selected_16:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 448 - 64
        self.y = (SCREEN_HEIGHT) // 2 - 280 + 256
        self.image = Slot_Inv_16_Selected
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Inv_c_Slot_Unselected_16:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 448 - 64
        self.y = (SCREEN_HEIGHT) // 2 - 280 + 256
        self.image = Slot_Inv_16_Unselected
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Inv_c_Slot_Selected_17:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 320 - 64
        self.y = (SCREEN_HEIGHT) // 2 - 280 + 256
        self.image = Slot_Inv_17_Selected
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Inv_c_Slot_Unselected_17:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 320 - 64
        self.y = (SCREEN_HEIGHT) // 2 - 280 + 256
        self.image = Slot_Inv_17_Unselected
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Inv_c_Slot_Selected_18:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 192 - 64
        self.y = (SCREEN_HEIGHT) // 2 - 280 + 256
        self.image = Slot_Inv_18_Selected
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Inv_c_Slot_Unselected_18:
    def __init__(self):
        self.x = (SCREEN_WIDTH) // 2 + 192 - 64
        self.y = (SCREEN_HEIGHT) // 2 - 280 + 256
        self.image = Slot_Inv_18_Unselected
        self.width = self.image.get_width()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))


