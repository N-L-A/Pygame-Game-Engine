import pygame

pygame.init()

screen_size = (1536, 801)


def fast_gif(img, workspace, pos=(0, 0), size=(100, 100), fps=12):
    """easy way to create one-time gif with only one line
     (warning, creating gifs using this way may slow down the program)"""
    if workspace.get_size() != screen_size:
        x = workspace.get_size()[0]
        y = workspace.get_size()[1]
        x = x / screen_size[0]
        y = y / screen_size[1]
        size = (size[0] * x, size[1] * y)
        pos = (pos[0] * x, pos[1] * y)
    t = pygame.time.get_ticks()
    i = len(img)
    tim = (1/fps)*1000
    i = i * tim
    i = t % i
    i = int(i / tim)
    workspace.blit(pygame.transform.scale(img[i], size), pos)


def init(screen_size_):
    """set the resolution (included in PE.init())"""
    global screen_size
    if type(screen_size_) == type((10, 10)) and len(screen_size_) == 2:
        screen_size = screen_size_
    else:
        print("init warn")


class Gif:
    """PE's gif is easy way to display looped animations from a list (of pygame surfaces)"""
    def __init__(self, img: list, pos=(0,0), size=(100,100), fps=12, color=(0, 0, 0, 0), rot=0):
        self.img = img
        self.pos = pos
        self.size = size
        self.fps = fps
        self.color = color
        self.rot = rot

    def show(self, workspace: pygame.Surface):
        """put the gif on a surface"""
        size = self.size
        pos = self.pos
        img = self.img
        fps = self.fps
        color = self.color
        if workspace.get_size() != screen_size:
            x = workspace.get_size()[0]
            y = workspace.get_size()[1]
            x = x/screen_size[0]
            y = y/screen_size[1]
            size = (size[0]*x, size[1]*y)
            pos = (pos[0]*x, pos[1]*y)
        t = pygame.time.get_ticks()
        i = len(img)
        tim = (1/fps)*1000
        i = i*tim
        i = t%i
        i = int(i/tim)
        img2 = pygame.transform.scale(img[i], size)
        img2 = pygame.transform.rotate(img2, self.rot)
        workspace.blit(img2, pos)
        if color[3] > 0:
            img2.fill(color)
            workspace.blit(img2, pos)

    def set_variables(self, img=None, pos=None, size=None, fps=None, color=None, rot=None):
        """change the gif's parameters"""
        if img:
            self.img = img
        if pos:
            self.pos = pos
        if size:
            self.size = size
        if fps:
            self.fps = fps
        if color:
            self.color = color
        if rot:
            self.rot = rot

    def get_image(self):
        """get the right frame as surface"""
        size = self.size
        pos = self.pos
        img = self.img
        fps = self.fps
        color = self.color
        t = pygame.time.get_ticks()
        i = len(img)
        tim = (1 / fps) * 1000
        i = i * tim
        i = t % i
        i = int(i / tim)
        img2 = pygame.transform.scale(img[i], size)
        img2 = pygame.transform.rotate(img2, self.rot)
        img3 = img2.copy()
        if color[3] > 0:
            img3.fill(color)
            img2.blit(img3, (0, 0))
        return img2
