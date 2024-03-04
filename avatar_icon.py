import pygame
from resources import DUCKING, RUNNING, JUMPING
from resources import DUCKING_BIRD, RUNNING_BIRD, JUMPING_BIRD
from resources import DUCKING_DUCK, RUNNING_DUCK, JUMPING_DUCK, Avatar, Avatar_Bird, Avatar_Duck


class DinosaurAvatarIcon:
    X_POS = 0
    Y_POS = 600

    def __init__(self):
        self.run_img = Avatar

        self.dino_run = True

        self.step_index = 0
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

    def update(self):
        if self.dino_run:
            self.run()

        if self.step_index >= 640:
            self.step_index = 0
            self.dino_run = True

    def run(self):
        self.image = self.run_img[self.step_index // 80]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 5

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))



class BirdAvatarIcon:
    X_POS = 0
    Y_POS = 600

    def __init__(self):
        self.run_img = Avatar_Bird

        self.dino_run = True

        self.step_index = 0
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

    def update(self):
        if self.dino_run:
            self.run()

        if self.step_index >= 120:
            self.step_index = 0
            self.dino_run = True

    def run(self):
        self.image = self.run_img[self.step_index // 24]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))


class DuckAvatarIcon:
    X_POS = 0
    Y_POS = 600

    def __init__(self):
        self.run_img = Avatar_Duck
        self.dino_run = True
        self.step_index = 0
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

    def update(self):
        if self.dino_run:
            self.run()

        if self.step_index >= 44_944:
            self.step_index = 0  # Setze den Index auf Null zurück
            self.dino_run = True

    def run(self):
        self.image = self.run_img[self.step_index // 212]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 300

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

