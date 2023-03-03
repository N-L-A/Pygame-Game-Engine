import pygame
from PE_tools import ImageTransformation

pygame.init()

screen_size = (1536, 801)

click = False


def init(screen_size_):
    """set the resolution (included in PE.init())"""
    global screen_size
    if type(screen_size_) == type((10, 10)) and len(screen_size_) == 2:
        screen_size = screen_size_
    else:
        print("init warn")


def frame_click():
    """update clicks, put in the main loop (after the update line (pygame.display.update()))
    known problem in case of not using this function:
    - clicks will always triggered until mouse up"""
    global click
    if pygame.mouse.get_pressed()[0]:
        click = True
    else:
        click = False


class ButtonTexture:
    """"""
    def __init__(self, image: pygame.Surface):
        self.texture = image
        size_y = image.get_size()[1]/3
        size = (image.get_size()[0], size_y)
        self.image_neutral = ImageTransformation.crop(image, size, (0, 0))
        self.image_hover = ImageTransformation.crop(image, size, (0, size_y))
        self.image_click = ImageTransformation.crop(image, size, (0, size_y*2))

    def __iter__(self):
        return [self.image_neutral, self.image_hover, self.image_click]

    def __getitem__(self, item):
        return [self.image_neutral, self.image_hover, self.image_click].__getitem__(item)


class Button(object):
    """add a button. you can write text or add image.
    set img to None to use auto background"""
    size = (10, 10)
    pos = (0, 0)
    img = None
    text = ""
    text_color = (0, 0, 0)
    text_size = 0
    hover = False
    click = False

    def show(self, workspace: pygame.Surface):
        """put the button on a surface (we recommend to use only the window)"""
        size = self.size
        pos = self.pos
        img = self.img
        if isinstance(img, pygame.Surface):
            img = self.img.copy()
        if workspace.get_size() != screen_size:
            x = workspace.get_size()[0]
            y = workspace.get_size()[1]
            x = x/screen_size[0]
            y = y/screen_size[1]
            size = (size[0]*x, size[1]*y)
            pos = (pos[0]*x, pos[1]*y)
        if isinstance(img, pygame.Surface):
            img = pygame.transform.scale(self.img, size)
            workspace.blit(img, pos)
        elif not img:
            pygame.draw.rect(workspace, self.back_color, (pos[0], pos[1], size[0], size[1]))
        font = pygame.font.Font(self.font, int(self.text_size*y))
        text = font.render(self.text, True, self.text_color)

        sizeX_txt = min(text.get_width(), size[0])
        sizeY_txt = min(size[1], text.get_height())
        posX_txt = max(size[0]/2-(text.get_width()/2), 0)
        posY_txt = max(size[1]/2-(text.get_height()/2), 0)
        txt_frame = pygame.Surface(text.get_size(), pygame.SRCALPHA)
        txt_frame.blit(text, (0, 0))
        txt_frame = pygame.transform.scale(txt_frame, (sizeX_txt, sizeY_txt))
        if not isinstance(img, ButtonTexture):
            workspace.blit(txt_frame, (pos[0]+posX_txt, pos[1]+posY_txt))
        if self.hover:
            frame = pygame.Surface(size, pygame.SRCALPHA)
            if self.click:
                if isinstance(img, ButtonTexture):
                    frame.blit(pygame.transform.scale(img[2], size), (0, 0))
                else:
                    frame.fill(self.click_color)
            else:
                if isinstance(img, ButtonTexture):
                    frame.blit(pygame.transform.scale(img[1], size), (0, 0))
                else:
                    frame.fill(self.hover_color)
            workspace.blit(frame, pos)
        elif isinstance(img, ButtonTexture):
            workspace.blit(pygame.transform.scale(img[0], size), pos)
        if isinstance(img, ButtonTexture):
            workspace.blit(txt_frame, (pos[0] + posX_txt, pos[1] + posY_txt))


    def __init__(self, pos=(0, 0), size=(20, 10), img=None, text="", text_color=(0, 0, 0), text_size=20,
                 font='freesansbold.ttf', hover_color=(255, 255, 255, 100), click_color=(0, 0, 0, 100),
                 back_color=(200, 200, 200)):
        self.pos = pos
        self.size = size
        self.img = img
        self.text = text
        self.text_color = text_color
        self.text_size = text_size
        self.font = font
        self.hover_color = hover_color
        self.click_color = click_color
        self.back_color = back_color

    def is_hover(self, workspace: pygame.Surface):
        """way to know if the mouse hover the button"""
        mp = pygame.mouse.get_pos()
        size = self.size
        pos = self.pos
        if workspace.get_size() != screen_size:
            x = workspace.get_size()[0]
            y = workspace.get_size()[1]
            x = x/screen_size[0]
            y = y/screen_size[1]
            size = (size[0]*x, size[1]*y)
            pos = (pos[0]*x, pos[1]*y)
        if pos[0] < mp[0] < pos[0]+size[0] and pos[1] < mp[1] < pos[1] + size[1]:
            self.hover = True
        else:
            self.hover = False
        return self.hover

    def is_clicked(self, workspace: pygame.Surface):
        """way to know if the mouse click the button"""
        self.is_hover(workspace)
        is_clicked = self.hover and pygame.mouse.get_pressed()[0]
        is_clicked = is_clicked and not click
        self.click = is_clicked
        return is_clicked

    def change_variables(self, pos=None, size=None, img=0, text=None, text_color=None, text_size=None,
                 font=None, hover_color=None, click_color=None):
        """change the parameters of the button (set image to 0 to don't chage the variable)"""
        if pos:
            self.pos = pos
        if size:
            self.size = size
        if img != 0:
            self.img = img
        if text:
            self.text = text
        if text_color:
            self.text_color = text_color
        if text_size:
            self.text_size = text_size
        if font:
            self.font = font
        if hover_color:
            self.hover_color = hover_color
        if click_color:
            self.click_color = click_color
