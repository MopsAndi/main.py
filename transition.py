import pygame
from settings import SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN
from resources import TRANSITION

class Transition:
    def __init__(self):
        self.x = SCREEN_WIDTH
        self.y = 0
        self.image = TRANSITION
        self.width = SCREEN_WIDTH - 1920
        self.move_speed = 85
        self.fade_speed = 5
        self.background_alpha = 0

    def update(self, SCREEN):
        if self.x <= self.width:
            self.x = 1920
            self.background_alpha = 0

        while self.x >= self.width:
            self.background_alpha = min(255, self.background_alpha + self.fade_speed)

            background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            background.fill((0, 0, 0, self.background_alpha))
            SCREEN.blit(background, (0, 0))

            self.x -= self.move_speed
            SCREEN.blit(self.image, (self.x, self.y))
            pygame.display.update()

            pygame.time.Clock().tick(160)

class Transition_left:
    def __init__(self):
        self.x = -SCREEN_WIDTH
        self.y = 0
        self.image = TRANSITION
        self.width = -SCREEN_WIDTH + 1920
        self.move_speed = 85
        self.fade_speed = 5
        self.background_alpha = 0

    def update(self, SCREEN):
        if self.x >= self.width:
            self.x = -1920
            self.background_alpha = 0

        while self.x <= self.width:
            self.background_alpha = min(255, self.background_alpha + self.fade_speed)

            background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            background.fill((0, 0, 0, self.background_alpha))
            SCREEN.blit(background, (0, 0))

            self.x += self.move_speed
            SCREEN.blit(self.image, (self.x, self.y))
            pygame.display.update()

            pygame.time.Clock().tick(160)
