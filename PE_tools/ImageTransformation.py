import pygame


def crop(img: pygame.Surface, size: tuple[int, int], pos=(0, 0)):
    """crop an image"""
    surface = pygame.Surface(size, pygame.SRCALPHA)
    surface.blit(img, (pos[0]*-1, pos[1]*-1))
    return surface


def blur(img: pygame.Surface, level: int):
    """blur an image"""
    size = img.get_size()
    surface = pygame.transform.smoothscale(pygame.transform.smoothscale(img, (size[0]/level, size[1]/level)), size)
    return surface


def pixelate(img: pygame.Surface, level: int):
    """pixelate an image"""
    size = img.get_size()
    surface = pygame.transform.scale(pygame.transform.scale(img, (size[0]/level, size[1]/level)), size)
    return surface


def tint(img: pygame.Surface, color: pygame.color, mode=pygame.BLEND_MULT):
    """tint an image"""
    img = img.copy()
    img.fill(color, special_flags=mode)
    return img


def tint_add(img: pygame.Surface, color: pygame.color):
    """tint an image with 'add' blending method"""
    img = img.copy()
    img.fill(color, special_flags=pygame.BLEND_ADD)
    return img


def tint_sub(img: pygame.Surface, color: pygame.color):
    """tint an image with 'sub' blending method"""
    img = img.copy()
    img.fill(color, special_flags=pygame.BLEND_SUB)
    return img


def tint_mul(img: pygame.Surface, color: pygame.color):
    """tint an image with 'mult' blending method"""
    img = img.copy()
    img.fill(color, special_flags=pygame.BLEND_MULT)
    return img


def tint_lighten(img: pygame.Surface, color: pygame.color):
    """tint an image with 'max' blending method"""
    img = img.copy()
    img.fill(color, special_flags=pygame.BLEND_MAX)
    return img


def tint_darken(img: pygame.Surface, color: pygame.color):
    """tint an image with 'min' blending method"""
    img = img.copy()
    img.fill(color, special_flags=pygame.BLEND_MIN)
    return img


def find_edges(img: pygame.Surface):
    """find the edges of an image using laplacian algorithm"""
    return pygame.transform.laplacian(img)


def scroll(img: pygame.Surface, offset: pygame.Vector2):
    """scroll the image in repeatable pattern"""

    m = img.get_size()
    s = img.get_size()
    a = list(s)
    offset = list(offset)
    if offset[0] < 0:
        offset[0] = (abs(offset[0])%m[0])*-1
        a[0] *= -1
    else:
        offset[0] = offset[0]%m[0]
    if offset[1] < 0:
        offset[1] = (abs(offset[1]) % m[1]) * -1
        a[1] *= -1
    else:
        offset[1] = offset[1]%m[1]
    surface = pygame.Surface(s, pygame.SRCALPHA)
    surface.blit(img, offset)
    if offset[0] != 0:
        surface.blit(img, (offset[0]-a[0], offset[1]))
    if offset[1] != 0:
        surface.blit(img, (offset[0], offset[1]-a[1]))
    if offset[1] != 0 and offset[0] != 0:
        surface.blit(img, (offset[0]-a[0], offset[1]-a[1]))
    return surface

