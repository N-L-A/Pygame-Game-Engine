import pygame

pygame.init()

screen_size = (1536, 801)


def init(screen_size_):
    """set the resolution (included in PE.init())"""
    global screen_size
    if type(screen_size_) == type((10, 10)) and len(screen_size_) == 2:
        screen_size = screen_size_
    else:
        print("init warn")


def draw_rect(win: pygame.Surface, pos=(0, 0), size=(10, 10), color=(0, 0, 255), border=5, rot=0):
    """draw a rect that align to the screen size on a surface"""
    frame = pygame.Surface(size, pygame.SRCALPHA)
    pygame.draw.rect(frame, color, ((0, 0), size), border)
    frame = pygame.transform.rotate(frame, rot)
    size = frame.get_size()
    if win.get_size() != screen_size:
        x = win.get_size()[0]
        y = win.get_size()[1]
        x = x / screen_size[0]
        y = y / screen_size[1]
        size = (size[0] * x, size[1] * y)
        pos = (pos[0] * x, pos[1] * y)
    frame = pygame.transform.scale(frame, size)
    win.blit(frame, pos)


def draw_circle(win: pygame.Surface, pos=(0, 0), radius=0, color=(0, 0, 255), border=5):
    """draw a rect that align to the screen size on a surface"""
    size = (radius*2, radius*2)
    frame = pygame.Surface(size, pygame.SRCALPHA)
    pygame.draw.circle(frame, color, (radius, radius), radius, border)
    if win.get_size() != screen_size:
        x = win.get_size()[0]
        y = win.get_size()[1]
        x = x / screen_size[0]
        y = y / screen_size[1]
        size = (size[0] * x, size[1] * y)
        pos = (pos[0] * x, pos[1] * y)
    frame = pygame.transform.scale(frame, size)
    win.blit(frame, pos)


def draw_shape(win: pygame.Surface, pos=(0, 0), points=((0, 0), (10, 10)), color=(0, 0, 255), border=5, rot=0):
    """draw shape from list of points, can be rotated and align to screen size"""
    size = (0, 0)
    p = points
    for x in p:
        size = (max(size[0], x[0]), max(size[1], x[1]))
    frame = pygame.Surface(size, pygame.SRCALPHA)
    pygame.draw.polygon(frame, color, p, border)
    frame = pygame.transform.rotate(frame, rot)
    size = frame.get_size()
    if win.get_size() != screen_size:
        x = win.get_size()[0]
        y = win.get_size()[1]
        x = x / screen_size[0]
        y = y / screen_size[1]
        size = (size[0] * x, size[1] * y)
        pos = (pos[0] * x, pos[1] * y)
    frame = pygame.transform.scale(frame, size)
    win.blit(frame, pos)


def draw_ellipse(win: pygame.Surface, pos=(0, 0), size=(10, 10),color=(0, 0, 255), border=5):
    """draw an ellipse that align to screen size"""
    frame = pygame.Surface(size, pygame.SRCALPHA)
    pygame.draw.ellipse(frame, color, ((0, 0), size), border)
    if win.get_size() != screen_size:
        x = win.get_size()[0]
        y = win.get_size()[1]
        x = x / screen_size[0]
        y = y / screen_size[1]
        size = (size[0] * x, size[1] * y)
        pos = (pos[0] * x, pos[1] * y)
    frame = pygame.transform.scale(frame, size)
    win.blit(frame, pos)


def draw_line(win: pygame.Surface, pos1=(0, 0), pos2=(10, 10), color=(0, 0, 255), size=5):
    """draw a line that align to the screen size"""
    f_size = (max(pos1[0], pos2[0])+size, max(pos1[1], pos2[1])+size)
    pos = (min(pos1[0], pos2[0]) - size, min(pos1[1], pos2[1]) - size)
    frame = pygame.Surface(f_size, pygame.SRCALPHA)
    pygame.draw.line(frame, color, pos1, pos2, size)
    size = f_size
    del f_size
    if win.get_size() != screen_size:
        x = win.get_size()[0]
        y = win.get_size()[1]
        x = x / screen_size[0]
        y = y / screen_size[1]
        size = (size[0] * x, size[1] * y)
        pos = (pos[0] * x, pos[1] * y)
    frame = pygame.transform.scale(frame, size)
    win.blit(frame, pos)


