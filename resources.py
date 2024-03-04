import pygame
import os


test = pygame.image.load(os.path.join("assets/Other", "hs.png"))

Inventory_Blank_Unselected = pygame.image.load(os.path.join("assets/Inventory", "Inv_1_Blank_Unselected.png"))
Inventory_Blank_Selected =  pygame.image.load(os.path.join("assets/Inventory", "Inv_1_Blank_Selected.png"))

#Test_button_selected =  pygame.image.load(os.path.join("assets/Other", "Test_Button_Selected.png"))
#Test_button_unselected =  pygame.image.load(os.path.join("assets/Other", "Test_Button_Unselected.png"))

BG_MAIN_MENU = pygame.image.load(os.path.join("assets/Other", "Background_Main_Menu.png"))
BG_MAIN_MENU_1 = pygame.image.load(os.path.join("assets/Other", "Background_Main_Menu1.png"))
TRANSITION = pygame.image.load(os.path.join("assets/Other", "Transition.png"))

BG = pygame.image.load(os.path.join("assets/Other", "Track.png"))

Avatar = [
    pygame.image.load(os.path.join("assets/Avatar", "Dino_Avatar.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Dino_Avatar.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Dino_Avatar.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Dino_Avatar.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Dino_Avatar.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Dino_Avatar.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Dino_Avatar.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Dino_Avatar_Closed.png")),
]

Avatar_Bird = [
    pygame.image.load(os.path.join("assets/Avatar", "Bird_Avatar_Closed.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Bird_Avatar_Closed.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Bird_Avatar_Closed.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Bird_Avatar_Open.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Bird_Avatar_Closed.png")),
]

Avatar_Duck = [
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_2.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_2.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_2.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_2.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_2.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_2.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_2.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_2.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_2.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_2.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_2.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_3.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_3.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_3.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_3.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_3.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_3.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_3.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_3.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_3.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_3.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_3.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_7.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_6.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_8.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_9.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_10.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_11.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_12.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_13.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_14.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_15.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_16.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_17.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_18.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_19.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_20.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_21.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_22.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_23.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_24.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_25.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_26.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_27.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_28.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_29.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_30.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_31.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_32.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_33.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_34.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_35.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_36.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_37.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_38.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_39.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_40.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_41.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_42.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_43.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_44.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_45.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_46.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_47.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_48.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_49.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_50.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_51.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_52.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_53.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_54.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_55.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_56.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_57.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_58.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_59.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_60.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_61.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_62.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_63.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_64.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_65.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_66.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_67.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_68.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_69.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_70.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_71.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_72.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_73.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_74.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_75.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_76.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_77.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_78.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_79.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_80.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_81.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_82.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_83.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_84.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_85.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_86.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_87.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_88.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_89.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_90.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_90.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_90.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_90.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_90.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_90.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_90.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_90.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_90.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_90.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_90.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_90.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
    pygame.image.load(os.path.join("assets/Avatar", "Duck_Avatar_1.png")),
]





RUNNING = [
    pygame.image.load(os.path.join("assets/Dino", "DinoRun1.png")),
    pygame.image.load(os.path.join("assets/Dino", "DinoRun2.png")),
    pygame.image.load(os.path.join("assets/Dino", "DinoRun1.png")),
    pygame.image.load(os.path.join("assets/Dino", "DinoRun2.png")),
]
JUMPING = pygame.image.load(os.path.join("assets/Dino", "DinoJump.png"))

DUCKING = [
    pygame.image.load(os.path.join("assets/Dino", "DinoDuck1.png")),
    pygame.image.load(os.path.join("assets/Dino", "DinoDuck2.png")),
    pygame.image.load(os.path.join("assets/Dino", "DinoDuck1.png")),
    pygame.image.load(os.path.join("assets/Dino", "DinoDuck2.png")),
]


RUNNING_BIRD = [
    pygame.image.load(os.path.join("assets/Dino_Skins/Bird_Dino_Skin", "DinoRun1.png")),
    pygame.image.load(os.path.join("assets/Dino_Skins/Bird_Dino_Skin", "DinoRun4.png")),
    pygame.image.load(os.path.join("assets/Dino_Skins/Bird_Dino_Skin", "DinoRun1.png")),
    pygame.image.load(os.path.join("assets/Dino_Skins/Bird_Dino_Skin", "DinoRun4.png")),
]


JUMPING_BIRD = pygame.image.load(os.path.join("assets/Dino_Skins/Bird_Dino_Skin", "DinoJump.png"))

DUCKING_BIRD = [
    pygame.image.load(os.path.join("assets/Dino_Skins/Bird_Dino_Skin", "DinoDuck1.png")),
    pygame.image.load(os.path.join("assets/Dino_Skins/Bird_Dino_Skin", "DinoDuck2.png")),
    pygame.image.load(os.path.join("assets/Dino_Skins/Bird_Dino_Skin", "DinoDuck1.png")),
    pygame.image.load(os.path.join("assets/Dino_Skins/Bird_Dino_Skin", "DinoDuck2.png")),
]


RUNNING_DUCK = [
    pygame.image.load(os.path.join("assets/Dino_Skins/Duck_Dino_Skin", "DinoRun1.png")),
    pygame.image.load(os.path.join("assets/Dino_Skins/Duck_Dino_Skin", "DinoRun3.png")),
    pygame.image.load(os.path.join("assets/Dino_Skins/Duck_Dino_Skin", "DinoRun2.png")),
    pygame.image.load(os.path.join("assets/Dino_Skins/Duck_Dino_Skin", "DinoRun3.png")),
]
JUMPING_DUCK = pygame.image.load(os.path.join("assets/Dino_Skins/Duck_Dino_Skin", "DinoJump.png"))

DUCKING_DUCK = [
    pygame.image.load(os.path.join("assets/Dino_Skins/Duck_Dino_Skin", "DinoDuck1.png")),
    pygame.image.load(os.path.join("assets/Dino_Skins/Duck_Dino_Skin", "DinoDuck2.png")),
    pygame.image.load(os.path.join("assets/Dino_Skins/Duck_Dino_Skin", "DinoDuck1.png")),
    pygame.image.load(os.path.join("assets/Dino_Skins/Duck_Dino_Skin", "DinoDuck2.png")),
]


SMALL_CACTUS = [
    pygame.image.load(os.path.join("assets/Cactus", "SmallCactus1.png")),
    pygame.image.load(os.path.join("assets/Cactus", "SmallCactus2.png")),
    pygame.image.load(os.path.join("assets/Cactus", "SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join("assets/Cactus", "LargeCactus1.png")),
    pygame.image.load(os.path.join("assets/Cactus", "LargeCactus2.png")),
    pygame.image.load(os.path.join("assets/Cactus", "LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join("assets/Bird", "Bird1.png")),
    pygame.image.load(os.path.join("assets/Bird", "Bird2.png")),
]


DOUBLE_POINTS = [
    pygame.image.load(os.path.join("assets/Powerups", "Double_Points1.png")),
    pygame.image.load(os.path.join("assets/Powerups", "Double_Points2.png")),
]






CLOUD = pygame.image.load(os.path.join("assets/Other", "Cloud.png"))

VANILLA_GAMEMODE_ICON_UNSELECTED = pygame.image.load(os.path.join("assets/Other", "icon_dino_vanilla_unselected.png"))
VANILLA_GAMEMODE_ICON_SELECTED = pygame.image.load(os.path.join("assets/Other", "icon_dino_vanilla_selected.png"))
CHALLENGER_GAMEMODE_ICON_SELECTED = pygame.image.load(os.path.join("assets/Other", "icon_dino_challengermode_selected.png"))
CHALLENGER_GAMEMODE_ICON_UNSELECTED = pygame.image.load(os.path.join("assets/Other", "icon_dino_challengermode_unselected.png"))
MULTIPLAYER_GAMEMODE_ICON_SELECTED = pygame.image.load(os.path.join("assets/Other", "icon_dino_multiplayermode_selected.png"))
MULTIPLAYER_GAMEMODE_ICON_UNSELECTED = pygame.image.load(os.path.join("assets/Other", "icon_dino_multiplayermode_unselected.png"))

DINO_SHOP_SELECTED = pygame.image.load(os.path.join("assets/Other", "Dino_Shop_Selected.png"))
DINO_SHOP_UNSELECTED = pygame.image.load(os.path.join("assets/Other", "Dino_Shop_Unselected.png"))
OBSTACLE_SHOP_SELECTED = pygame.image.load(os.path.join("assets/Other", "Obstacle_Shop_Selected.png"))
OBSTACLE_SHOP_UNSELECTED = pygame.image.load(os.path.join("assets/Other", "Obstacle_Shop_Unselected.png"))
BIRD_SHOP_SELECTED = pygame.image.load(os.path.join("assets/Other", "Bird_Shop_Selected.png"))
BIRD_SHOP_UNSELECTED = pygame.image.load(os.path.join("assets/Other", "Bird_Shop_Unselected.png"))
TRACK_SHOP_SELECTED = pygame.image.load(os.path.join("assets/Other", "Track_Shop_Selected.png"))
TRACK_SHOP_UNSELECTED = pygame.image.load(os.path.join("assets/Other", "Track_Shop_Unselected.png"))
POWER_UP_SHOP_SELECTED = pygame.image.load(os.path.join("assets/Other", "Power_Up_Shop_Selected.png"))
POWER_UP_SHOP_UNSELECTED = pygame.image.load(os.path.join("assets/Other", "Power_Up_Shop_Unselected.png"))

SHOP_BLANK_SELECTED = pygame.image.load(os.path.join("assets/Other", "Blank_Selected.png"))
SHOP_STATS_STATIC = pygame.image.load(os.path.join("assets/Shop/Stats", "Stats_Shop_Static.png"))

BUY_BUTTON_UNSELECTED = pygame.image.load(os.path.join("assets/Shop", "Buy_Button_Unselected.png"))
BUY_BUTTON_SELECTED = pygame.image.load(os.path.join("assets/Shop", "Buy_Button_Selected.png"))
BUY_BUTTON_PRESSED = pygame.image.load(os.path.join("assets/Shop", "Buy_Button_Pressed.png"))

SHOP_BLANK_UNSELECTED = pygame.image.load(os.path.join("assets/Other", "Blank_Unselected.png"))
SHOP_D_Skin1_UNSELECTED = pygame.image.load(os.path.join("assets/Shop/Dino_Skin_Icon", "Dino_Skin1_Icon_Unselected.png"))
SHOP_D_Skin1_SELECTED = pygame.image.load(os.path.join("assets/Shop/Dino_Skin_Icon", "Dino_Skin1_Icon_Selected.png"))
SHOP_D_Skin2_UNSELECTED = pygame.image.load(os.path.join("assets/Shop/Dino_Skin_Icon", "Dino_Skin2_Icon_Unselected.png"))
SHOP_D_Skin2_SELECTED = pygame.image.load(os.path.join("assets/Shop/Dino_Skin_Icon", "Dino_Skin2_Icon_Selected.png"))
SHOP_D_Skin3_UNSELECTED = pygame.image.load(os.path.join("assets/Shop/Dino_Skin_Icon", "Dino_Skin3_Icon_Unselected.png"))
SHOP_D_Skin3_SELECTED = pygame.image.load(os.path.join("assets/Shop/Dino_Skin_Icon", "Dino_Skin3_Icon_Selected.png"))
SHOP_D_Skin4_UNSELECTED = pygame.image.load(os.path.join("assets/Shop/Dino_Skin_Icon", "Dino_Skin4_Icon_Unselected.png"))
SHOP_D_Skin4_SELECTED = pygame.image.load(os.path.join("assets/Shop/Dino_Skin_Icon", "Dino_Skin4_Icon_Selected.png"))
SHOP_D_Skin5_UNSELECTED = pygame.image.load(os.path.join("assets/Shop/Dino_Skin_Icon", "Dino_Skin5_Icon_Unselected.png"))
SHOP_D_Skin5_SELECTED = pygame.image.load(os.path.join("assets/Shop/Dino_Skin_Icon", "Dino_Skin5_Icon_Selected.png"))

SHOP_O_Skin1_UNSELECTED = pygame.image.load(os.path.join("assets/Shop/Obstacles_Skin_Icon", "Obstacles_Skin1_Icon_Unselected.png"))
SHOP_O_Skin1_SELECTED = pygame.image.load(os.path.join("assets/Shop/Obstacles_Skin_Icon", "Obstacles_Skin1_Icon_Selected.png"))
SHOP_O_Skin2_UNSELECTED = pygame.image.load(os.path.join("assets/Shop/Obstacles_Skin_Icon", "Obstacles_Skin2_Icon_Unselected.png"))
SHOP_O_Skin2_SELECTED = pygame.image.load(os.path.join("assets/Shop/Obstacles_Skin_Icon", "Obstacles_Skin2_Icon_Selected.png"))
SHOP_O_Skin3_UNSELECTED = pygame.image.load(os.path.join("assets/Shop/Obstacles_Skin_Icon", "Obstacles_Skin3_Icon_Unselected.png"))
SHOP_O_Skin3_SELECTED = pygame.image.load(os.path.join("assets/Shop/Obstacles_Skin_Icon", "Obstacles_Skin3_Icon_Selected.png"))
SHOP_O_Skin4_UNSELECTED = pygame.image.load(os.path.join("assets/Shop/Obstacles_Skin_Icon", "Obstacles_Skin4_Icon_Unselected.png"))
SHOP_O_Skin4_SELECTED = pygame.image.load(os.path.join("assets/Shop/Obstacles_Skin_Icon", "Obstacles_Skin4_Icon_Selected.png"))
SHOP_O_Skin5_UNSELECTED = pygame.image.load(os.path.join("assets/Shop/Obstacles_Skin_Icon", "Obstacles_Skin5_Icon_Unselected.png"))
SHOP_O_Skin5_SELECTED = pygame.image.load(os.path.join("assets/Shop/Obstacles_Skin_Icon", "Obstacles_Skin5_Icon_Selected.png"))

SHOP_B_Skin1_UNSELECTED = pygame.image.load(os.path.join("assets/Shop/Bird_Skin_Icon", "Bird_Skin1_Icon_Unselected.png"))
SHOP_B_Skin1_SELECTED = pygame.image.load(os.path.join("assets/Shop/Bird_Skin_Icon", "Bird_Skin1_Icon_Selected.png"))
SHOP_B_Skin2_UNSELECTED = pygame.image.load(os.path.join("assets/Shop/Bird_Skin_Icon", "Bird_Skin2_Icon_Unselected.png"))
SHOP_B_Skin2_SELECTED = pygame.image.load(os.path.join("assets/Shop/Bird_Skin_Icon", "Bird_Skin2_Icon_Selected.png"))
SHOP_B_Skin3_UNSELECTED = pygame.image.load(os.path.join("assets/Shop/Bird_Skin_Icon", "Bird_Skin3_Icon_Unselected.png"))
SHOP_B_Skin3_SELECTED = pygame.image.load(os.path.join("assets/Shop/Bird_Skin_Icon", "Bird_Skin3_Icon_Selected.png"))
SHOP_B_Skin4_UNSELECTED = pygame.image.load(os.path.join("assets/Shop/Bird_Skin_Icon", "Bird_Skin4_Icon_Unselected.png"))
SHOP_B_Skin4_SELECTED = pygame.image.load(os.path.join("assets/Shop/Bird_Skin_Icon", "Bird_Skin4_Icon_Selected.png"))
SHOP_B_Skin5_UNSELECTED = pygame.image.load(os.path.join("assets/Shop/Bird_Skin_Icon", "Bird_Skin5_Icon_Unselected.png"))
SHOP_B_Skin5_SELECTED = pygame.image.load(os.path.join("assets/Shop/Bird_Skin_Icon", "Bird_Skin5_Icon_Selected.png"))

SHOP_T_Skin1_UNSELECTED = pygame.image.load(os.path.join("assets/Shop/Track_Skin_Icon", "Track_Skin1_Icon_Unselected.png"))
SHOP_T_Skin1_SELECTED = pygame.image.load(os.path.join("assets/Shop/Track_Skin_Icon", "Track_Skin1_Icon_Selected.png"))
SHOP_T_Skin2_UNSELECTED = pygame.image.load(os.path.join("assets/Shop/Track_Skin_Icon", "Track_Skin2_Icon_Unselected.png"))
SHOP_T_Skin2_SELECTED = pygame.image.load(os.path.join("assets/Shop/Track_Skin_Icon", "Track_Skin2_Icon_Selected.png"))
SHOP_T_Skin3_UNSELECTED = pygame.image.load(os.path.join("assets/Shop/Track_Skin_Icon", "Track_Skin3_Icon_Unselected.png"))
SHOP_T_Skin3_SELECTED = pygame.image.load(os.path.join("assets/Shop/Track_Skin_Icon", "Track_Skin3_Icon_Selected.png"))
SHOP_T_Skin4_UNSELECTED = pygame.image.load(os.path.join("assets/Shop/Track_Skin_Icon", "Track_Skin4_Icon_Unselected.png"))
SHOP_T_Skin4_SELECTED = pygame.image.load(os.path.join("assets/Shop/Track_Skin_Icon", "Track_Skin4_Icon_Selected.png"))
SHOP_T_Skin5_UNSELECTED = pygame.image.load(os.path.join("assets/Shop/Track_Skin_Icon", "Track_Skin5_Icon_Unselected.png"))
SHOP_T_Skin5_SELECTED = pygame.image.load(os.path.join("assets/Shop/Track_Skin_Icon", "Track_Skin5_Icon_Selected.png"))

SHOP_P_Skin1_UNSELECTED = pygame.image.load(os.path.join("assets/Shop/Powerup_Skin_Icon", "Powerup_Skin1_Icon_Unselected.png"))
SHOP_P_Skin1_SELECTED = pygame.image.load(os.path.join("assets/Shop/Powerup_Skin_Icon", "Powerup_Skin1_Icon_Selected.png"))
SHOP_P_Skin2_UNSELECTED = pygame.image.load(os.path.join("assets/Shop/Powerup_Skin_Icon", "Powerup_Skin2_Icon_Unselected.png"))
SHOP_P_Skin2_SELECTED = pygame.image.load(os.path.join("assets/Shop/Powerup_Skin_Icon", "Powerup_Skin2_Icon_Selected.png"))
SHOP_P_Skin3_UNSELECTED = pygame.image.load(os.path.join("assets/Shop/Powerup_Skin_Icon", "Powerup_Skin3_Icon_Unselected.png"))
SHOP_P_Skin3_SELECTED = pygame.image.load(os.path.join("assets/Shop/Powerup_Skin_Icon", "Powerup_Skin3_Icon_Selected.png"))
SHOP_P_Skin4_UNSELECTED = pygame.image.load(os.path.join("assets/Shop/Powerup_Skin_Icon", "Powerup_Skin4_Icon_Unselected.png"))
SHOP_P_Skin4_SELECTED = pygame.image.load(os.path.join("assets/Shop/Powerup_Skin_Icon", "Powerup_Skin4_Icon_Selected.png"))
SHOP_P_Skin5_UNSELECTED = pygame.image.load(os.path.join("assets/Shop/Powerup_Skin_Icon", "Powerup_Skin5_Icon_Unselected.png"))
SHOP_P_Skin5_SELECTED = pygame.image.load(os.path.join("assets/Shop/Powerup_Skin_Icon", "Powerup_Skin5_Icon_Selected.png"))

START_GAME_UNSELECTED = pygame.image.load(os.path.join("assets/Other", "Startgame_Unselected.png"))
START_GAME_SELECTED = pygame.image.load(os.path.join("assets/Other", "Startgame_selected.png"))

SHOP_ICON_UNSELECTED = pygame.image.load(os.path.join("assets/Other", "Shop_Icon_Unselected.png"))
SHOP_ICON_SELECTED = pygame.image.load(os.path.join("assets/Other", "Shop_Icon_selected.png"))

QUIT_UNSELECTED = pygame.image.load(os.path.join("assets/Other", "Quit_Unselected.png"))
QUIT_SELECTED = pygame.image.load(os.path.join("assets/Other", "Quit_Selected.png"))

INVENTORY_ICON_UNSELECTED = pygame.image.load(os.path.join("assets/Other", "Inventory_Icon_Unselected.png"))
INVENTORY_ICON_SELECTED = pygame.image.load(os.path.join("assets/Other", "Inventory_Icon_Selected.png"))

SETTINGS_ICON_UNSELECTED = pygame.image.load(os.path.join("assets/Other", "settings_button_unselected.png"))
SETTINGS_ICON_SELECTED = pygame.image.load(os.path.join("assets/Other", "settings_button_selected.png"))


###Inv slots

Slot_Inv_1_Unselected = pygame.image.load(os.path.join("assets/Inventory", "Inv_1_Blank_Unselected.png"))
Slot_Inv_1_Selected = pygame.image.load(os.path.join("assets/Inventory", "Inv_1_Blank_Selected.png"))
Slot_Inv_2_Unselected = pygame.image.load(os.path.join("assets/Inventory", "Inv_2_Blank_Unselected.png"))
Slot_Inv_2_Selected = pygame.image.load(os.path.join("assets/Inventory", "Inv_2_Blank_Selected.png"))
Slot_Inv_3_Unselected = pygame.image.load(os.path.join("assets/Inventory", "Inv_3_Blank_Unselected.png"))
Slot_Inv_3_Selected = pygame.image.load(os.path.join("assets/Inventory", "Inv_3_Blank_Selected.png"))
Slot_Inv_4_Unselected = pygame.image.load(os.path.join("assets/Inventory", "Inv_4_Blank_Unselected.png"))
Slot_Inv_4_Selected = pygame.image.load(os.path.join("assets/Inventory", "Inv_4_Blank_Selected.png"))
Slot_Inv_5_Unselected = pygame.image.load(os.path.join("assets/Inventory", "Inv_5_Blank_Unselected.png"))
Slot_Inv_5_Selected = pygame.image.load(os.path.join("assets/Inventory", "Inv_5_Blank_Selected.png"))
Slot_Inv_6_Unselected = pygame.image.load(os.path.join("assets/Inventory", "Inv_6_Blank_Unselected.png"))
Slot_Inv_6_Selected = pygame.image.load(os.path.join("assets/Inventory", "Inv_6_Blank_Selected.png"))
Slot_Inv_7_Unselected = pygame.image.load(os.path.join("assets/Inventory", "Inv_7_Blank_Unselected.png"))
Slot_Inv_7_Selected = pygame.image.load(os.path.join("assets/Inventory", "Inv_7_Blank_Selected.png"))
Slot_Inv_8_Unselected = pygame.image.load(os.path.join("assets/Inventory", "Inv_8_Blank_Unselected.png"))
Slot_Inv_8_Selected = pygame.image.load(os.path.join("assets/Inventory", "Inv_8_Blank_Selected.png"))
Slot_Inv_9_Unselected = pygame.image.load(os.path.join("assets/Inventory", "Inv_9_Blank_Unselected.png"))
Slot_Inv_9_Selected = pygame.image.load(os.path.join("assets/Inventory", "Inv_9_Blank_Selected.png"))
Slot_Inv_10_Unselected = pygame.image.load(os.path.join("assets/Inventory", "Inv_10_Blank_Unselected.png"))
Slot_Inv_10_Selected = pygame.image.load(os.path.join("assets/Inventory", "Inv_10_Blank_Selected.png"))
Slot_Inv_11_Unselected = pygame.image.load(os.path.join("assets/Inventory", "Inv_11_Blank_Unselected.png"))
Slot_Inv_11_Selected = pygame.image.load(os.path.join("assets/Inventory", "Inv_11_Blank_Selected.png"))
Slot_Inv_12_Unselected = pygame.image.load(os.path.join("assets/Inventory", "Inv_12_Blank_Unselected.png"))
Slot_Inv_12_Selected = pygame.image.load(os.path.join("assets/Inventory", "Inv_12_Blank_Selected.png"))
Slot_Inv_13_Unselected = pygame.image.load(os.path.join("assets/Inventory", "Inv_13_Blank_Unselected.png"))
Slot_Inv_13_Selected = pygame.image.load(os.path.join("assets/Inventory", "Inv_13_Blank_Selected.png"))
Slot_Inv_14_Unselected = pygame.image.load(os.path.join("assets/Inventory", "Inv_14_Blank_Unselected.png"))
Slot_Inv_14_Selected = pygame.image.load(os.path.join("assets/Inventory", "Inv_14_Blank_Selected.png"))
Slot_Inv_15_Unselected = pygame.image.load(os.path.join("assets/Inventory", "Inv_15_Blank_Unselected.png"))
Slot_Inv_15_Selected = pygame.image.load(os.path.join("assets/Inventory", "Inv_15_Blank_Selected.png"))
Slot_Inv_16_Unselected = pygame.image.load(os.path.join("assets/Inventory", "Inv_16_Blank_Unselected.png"))
Slot_Inv_16_Selected = pygame.image.load(os.path.join("assets/Inventory", "Inv_16_Blank_Selected.png"))
Slot_Inv_17_Unselected = pygame.image.load(os.path.join("assets/Inventory", "Inv_17_Blank_Unselected.png"))
Slot_Inv_17_Selected = pygame.image.load(os.path.join("assets/Inventory", "Inv_17_Blank_Selected.png"))
Slot_Inv_18_Unselected = pygame.image.load(os.path.join("assets/Inventory", "Inv_18_Blank_Unselected.png"))
Slot_Inv_18_Selected = pygame.image.load(os.path.join("assets/Inventory", "Inv_18_Blank_Selected.png"))
Slot_Inv_19_Unselected = pygame.image.load(os.path.join("assets/Inventory", "Inv_19_Blank_Unselected.png"))
Slot_Inv_19_Selected = pygame.image.load(os.path.join("assets/Inventory", "Inv_19_Blank_Selected.png"))
Slot_Inv_20_Unselected = pygame.image.load(os.path.join("assets/Inventory", "Inv_20_Blank_Unselected.png"))
Slot_Inv_20_Selected = pygame.image.load(os.path.join("assets/Inventory", "Inv_20_Blank_Selected.png"))
Slot_Inv_21_Unselected = pygame.image.load(os.path.join("assets/Inventory", "Inv_21_Blank_Unselected.png"))
Slot_Inv_21_Selected = pygame.image.load(os.path.join("assets/Inventory", "Inv_21_Blank_Selected.png"))
Slot_Inv_22_Unselected = pygame.image.load(os.path.join("assets/Inventory", "Inv_22_Blank_Unselected.png"))
Slot_Inv_22_Selected = pygame.image.load(os.path.join("assets/Inventory", "Inv_22_Blank_Selected.png"))
Slot_Inv_23_Unselected = pygame.image.load(os.path.join("assets/Inventory", "Inv_23_Blank_Unselected.png"))
Slot_Inv_23_Selected = pygame.image.load(os.path.join("assets/Inventory", "Inv_23_Blank_Selected.png"))
Slot_Inv_24_Unselected = pygame.image.load(os.path.join("assets/Inventory", "Inv_24_Blank_Unselected.png"))
Slot_Inv_24_Selected = pygame.image.load(os.path.join("assets/Inventory", "Inv_24_Blank_Selected.png"))
Slot_Inv_25_Unselected = pygame.image.load(os.path.join("assets/Inventory", "Inv_25_Blank_Unselected.png"))
Slot_Inv_25_Selected = pygame.image.load(os.path.join("assets/Inventory", "Inv_25_Blank_Selected.png"))
Slot_Inv_26_Unselected = pygame.image.load(os.path.join("assets/Inventory", "Inv_26_Blank_Unselected.png"))
Slot_Inv_26_Selected = pygame.image.load(os.path.join("assets/Inventory", "Inv_26_Blank_Selected.png"))
Slot_Inv_27_Unselected = pygame.image.load(os.path.join("assets/Inventory", "Inv_27_Blank_Unselected.png"))
Slot_Inv_27_Selected = pygame.image.load(os.path.join("assets/Inventory", "Inv_27_Blank_Selected.png"))
Slot_Inv_28_Unselected = pygame.image.load(os.path.join("assets/Inventory", "Inv_28_Blank_Unselected.png"))
Slot_Inv_28_Selected = pygame.image.load(os.path.join("assets/Inventory", "Inv_28_Blank_Selected.png"))
Slot_Inv_29_Unselected = pygame.image.load(os.path.join("assets/Inventory", "Inv_29_Blank_Unselected.png"))
Slot_Inv_29_Selected = pygame.image.load(os.path.join("assets/Inventory", "Inv_29_Blank_Selected.png"))
Slot_Inv_30_Unselected = pygame.image.load(os.path.join("assets/Inventory", "Inv_30_Blank_Unselected.png"))
Slot_Inv_30_Selected = pygame.image.load(os.path.join("assets/Inventory", "Inv_30_Blank_Selected.png"))
Slot_Inv_31_Unselected = pygame.image.load(os.path.join("assets/Inventory", "Inv_31_Blank_Unselected.png"))
Slot_Inv_31_Selected = pygame.image.load(os.path.join("assets/Inventory", "Inv_31_Blank_Selected.png"))
Slot_Inv_32_Unselected = pygame.image.load(os.path.join("assets/Inventory", "Inv_32_Blank_Unselected.png"))
Slot_Inv_32_Selected = pygame.image.load(os.path.join("assets/Inventory", "Inv_32_Blank_Selected.png"))
Slot_Inv_33_Unselected = pygame.image.load(os.path.join("assets/Inventory", "Inv_33_Blank_Unselected.png"))
Slot_Inv_33_Selected = pygame.image.load(os.path.join("assets/Inventory", "Inv_33_Blank_Selected.png"))
Slot_Inv_34_Unselected = pygame.image.load(os.path.join("assets/Inventory", "Inv_34_Blank_Unselected.png"))
Slot_Inv_34_Selected = pygame.image.load(os.path.join("assets/Inventory", "Inv_34_Blank_Selected.png"))
Slot_Inv_35_Unselected = pygame.image.load(os.path.join("assets/Inventory", "Inv_35_Blank_Unselected.png"))
Slot_Inv_35_Selected = pygame.image.load(os.path.join("assets/Inventory", "Inv_35_Blank_Selected.png"))
Slot_Inv_36_Unselected = pygame.image.load(os.path.join("assets/Inventory", "Inv_36_Blank_Unselected.png"))
Slot_Inv_36_Selected = pygame.image.load(os.path.join("assets/Inventory", "Inv_36_Blank_Selected.png"))
