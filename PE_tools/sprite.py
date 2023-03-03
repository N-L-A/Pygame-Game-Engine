import pygame
from PE_tools import gifsPG

pygame.init()

screen_size = (1536, 801)


def init(screen_size_):
    """set the resolution (included in PE.init())"""
    global screen_size
    if type(screen_size_) == type((10, 10)) and len(screen_size_) == 2:
        screen_size = screen_size_
    else:
        print("init warn")


sprites = pygame.sprite.Group()
all_sprites = []


def show_all(workspace: pygame.Surface):
    """show all sprites"""
    for x in all_sprites:
        x.update()
    sprites.draw(workspace)


class Image:
    """single image sprite"""
    sprite = pygame.sprite.Sprite()

    def __init__(self, img: pygame.Surface, pos=(0, 0), size=(10, 10), rot=0):
        all_sprites.append(self)
        self.img = img
        self.pos = pos
        self.size = size
        self.rot = rot

    def update(self):
        """update parameters, put in main_loop"""
        win = pygame.display.get_window_size()
        size = self.size
        pos = self.pos
        if win != screen_size:
            x = win[0]
            y = win[1]
            x = x / screen_size[0]
            y = y / screen_size[1]
            size = (size[0] * x, size[1] * y)
            pos = (pos[0] * x, pos[1] * y)
        img = pygame.transform.rotate(pygame.transform.scale(self.img, size), self.rot)
        self.sprite.image = img
        self.sprite.rect = pos
        if not sprites.has(self.sprite):
            sprites.add(self.sprite)


class Animated:
    """use PGgifs to animate a sprite"""
    sprite = pygame.sprite.Sprite()

    def __init__(self, animation: gifsPG.Gif, pos=(0, 0), size=(10, 10), rot=0):
        all_sprites.append(self)
        self.img = animation.get_image()
        self.pos = pos
        self.size = size
        self.rot = rot
        self.animation = animation

    def update(self):
        """update parameters, put in main_loop"""
        win = pygame.display.get_window_size()
        size = self.size
        pos = self.pos
        if win != screen_size:
            x = win[0]
            y = win[1]
            x = x / screen_size[0]
            y = y / screen_size[1]
            size = (size[0] * x, size[1] * y)
            pos = (pos[0] * x, pos[1] * y)
        img = pygame.transform.rotate(pygame.transform.scale(self.animation.get_image(), size), self.rot)
        self.sprite.image = img
        self.sprite.rect = pos
        if not sprites.has(self.sprite):
            sprites.add(self.sprite)
