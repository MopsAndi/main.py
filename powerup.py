import random
from settings import SCREEN_WIDTH, GAME_SPEED

class Powerup_1:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH + 340

    def update(self, powerup1):
        self.rect.x -= GAME_SPEED
        if self.rect.x < -self.rect.width:
            powerup1.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)

class Double_Points1(Powerup_1):
    Powerup_HEIGHTS = [515, 523, 111111527, 11111111, 1111111 ,1111111]

    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = random.choice(self.Powerup_HEIGHTS)
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 40:
            self.index = 0
        SCREEN.blit(self.image[self.index // 20], self.rect)
        self.index += 1
