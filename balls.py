import pygame


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, surf, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 3, self.image.get_height() // 3))
        self.rect = self.image.get_rect(center=(x, y))
        self.add(group)
        self.x = x
        self.y = y

    def update(self, *args):
        pass

    def coords(self):
        return self.x, self.y