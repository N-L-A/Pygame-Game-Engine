import sys
import pygame
import time
from PE_tools import Draw, Buttons


pygame.init()

screen_size = (1536, 801)


def init(screen_size_):
    """set the resolution (included in PE.init())"""
    global screen_size
    if type(screen_size_) == type((10, 10)) and len(screen_size_) == 2:
        screen_size = screen_size_
    else:
        print("init warn")


def fast_image(workspace, img: pygame.surface.Surface, size=(100, 100), pos=(0, 0), rot=0, color=(0, 0, 0, 0)):
    """easy way to create PE image in only one line."""
    if workspace.get_size() != screen_size:
        x = workspace.get_size()[0]
        y = workspace.get_size()[1]
        x = x/screen_size[0]
        y = y/screen_size[1]
        size = (size[0]*x, size[1]*y)
        pos = (pos[0]*x, pos[1]*y)
    img = pygame.transform.scale(img, size)
    img = pygame.transform.rotate(img, rot)
    workspace.blit(img, pos)
    if color[3] > 0:
        img.fill(color)
        workspace.blit(img, pos)


def fast_text(workspace, text: str, size=10, color=(0, 0, 0), pos=(0, 0), dir=0, font='freesansbold.ttf'):
    """easy way to create PE text in only one line."""
    font = pygame.font.Font(font, int(size))  # freesansbold
    text = font.render(text, True, color)
    frame = pygame.Surface(text.get_size(), pygame.SRCALPHA)
    frame.blit(text, (0, 0))
   # s1 = frame.get_width() / 2
    #s2 = frame.get_height() / 2
    if workspace.get_size() != screen_size:
        x = workspace.get_size()[0]
        y = workspace.get_size()[1]
        x = x / screen_size[0]
        y = y / screen_size[1]
        back_size = (frame.get_size()[0] * x, frame.get_size()[1] * y)
        back_pos = (pos[0] * x, pos[1] * y)
    new_frame = pygame.transform.scale(frame, back_size)
    if dir == 0:
        workspace.blit(new_frame, back_pos)
    else:
        s1 = back_size[0] / 2
        s2 = back_size[1] / 2
        workspace.blit(new_frame, (back_pos[0] - s1, back_pos[1] - s2))


class TextLabel:
    """PE texts are better than regular pygame's texts.
    you can rotate them, add background, align transform to the screen and a lot more
    with only 2 lines!"""
    def __init__(self, text: str, size=10, color=(0, 0, 0), pos=(0, 0), dir=0, font='freesansbold.ttf',
                 background_color=(255, 255, 255, 0), rotation=0):
        self.text = text
        self.size = size
        self.color = color
        self.pos = pos
        self.dir = dir
        self.font = pygame.font.Font(font, int(size))
        self.background_color = background_color
        self.rotation = rotation

    def show(self, workspace: pygame.Surface):
        """put the text on a surface"""
        pos = self.pos
        text = self.text
        font = self.font
        color = self.color
        dir = self.dir
        back_col = self.background_color
        rot = self.rotation
        text = font.render(text, True, color)
        frame = pygame.Surface(text.get_size(), pygame.SRCALPHA)
        frame.fill(back_col)
        frame.blit(text, (0, 0))
        if workspace.get_size() != screen_size:
            x = workspace.get_size()[0]
            y = workspace.get_size()[1]
            x = x/screen_size[0]
            y = y/screen_size[1]
            back_size = (frame.get_size()[0]*x, frame.get_size()[1]*y)
            back_pos = (pos[0]*x, pos[1]*y)
        new_frame = pygame.transform.scale(frame, back_size)
        new_frame = pygame.transform.rotate(new_frame, rot)
        if dir == 0:
            workspace.blit(new_frame, back_pos)
        else:
            s1 = back_size[0]/2
            s2 = back_size[1]/2
            workspace.blit(new_frame, (pos[0]-s1, pos[1]-s2))

    def set_variables(self, text=None, size=None, color=None, pos=None, dir=None, font=None, background_color=None,
                      rotation=None):
        """change the parameters of the text object"""
        if text:
            self.text = text
        if size:
            self.size = size
        if color:
            self.color = color
        if pos:
            self.pos = pos
        if dir:
            self.dir = dir
        if font:
            self.font = pygame.font.Font(font, int(size))
        if background_color:
            self.background_color = background_color
        if rotation:
            self.rotation = rotation


class Image:
    """PE images are better than regular pygame's images.
        you can rotate them, add tint, align transform to the screen and more
        with only 2 lines!"""
    def __init__(self, img: pygame.Surface, size=(100, 100), pos=(0, 0), rot=0, color=(0, 0, 0, 0)):
        self.img = img
        self.size = size
        self.pos = pos
        self.rot = rot
        self.color = color

    def show(self, workspace: pygame.Surface):
        """put the text on a surface"""
        size = self.size
        img = self.img
        pos = self.pos
        rot = self.rot
        color = self.color
        if workspace.get_size() != screen_size:
            x = workspace.get_size()[0]
            y = workspace.get_size()[1]
            x = x/screen_size[0]
            y = y/screen_size[1]
            size = (size[0]*x, size[1]*y)
            pos = (pos[0]*x, pos[1]*y)
        img = pygame.transform.scale(img, size)
        img = pygame.transform.rotate(img, rot)
        workspace.blit(img, pos)
        if color[3] > 0:
            img.fill(color)
            workspace.blit(img, pos)

    def set_variables(self, img=None, size=None, pos=None, rot=None, color=None):
        if img:
            self.img = img
        if size:
            self.size = size
        if pos:
            self.pos = pos
        if rot:
            self.rot = rot
        if color:
            self.color = color


class InputLabel:
    """input label are great way to collect input using GUI!"""
    user_text = ''
    select_pos = 0
    min_box_size = (100, 32)
    base_font = pygame.font.Font(None, min_box_size[1])
    input_rect = pygame.Rect(200, 200, 140, min_box_size[1])
    none_sel_text = "Enter text here:"
    color_active = (200, 200, 200)
    color_active_text = (0, 0, 0)
    color_passive = (100, 100, 100)
    color_passive_text = (255, 255, 255)
    color = color_passive
    text_color = color_passive_text
    active = False

    def __init__(self, size=(100, 32), pos=(200, 200), box_text="Enter text here:", col_active=(200, 200, 200),
             col_passive=(100, 100, 100), col_active_txt=None, col_passive_txt=None):
        self.min_box_size = size
        self.none_sel_text = box_text
        self.color_active = col_active
        self.color_passive = col_passive
        if type(col_active_txt) != type((0, 0, 0)) and type(col_passive_txt) != type(pygame.color.Color(0, 0, 0)):
            self.color_active_text = (abs(255-col_active[0]), abs(255-col_active[1]), abs(255-col_active[2]))
        else:
            self.color_active_text = col_active_txt
        if type(col_passive_txt) != type((0, 0, 0)) and type(col_passive_txt) != type(pygame.color.Color(0, 0, 0)):
            self.color_passive_text = (abs(255-col_passive[0]), abs(255-col_passive[1]), abs(255-col_passive[2]))
        else:
            self.color_passive_text = col_passive_txt
        self.base_font = pygame.font.Font(None, self.min_box_size[1])
        self.input_rect = pygame.Rect(0, 0, 140, self.min_box_size[1])
        self.pos = pos

    def show(self, workspace, events):
        """put the input label on a surface"""
        ratioX = pygame.display.get_window_size()[0]/screen_size[0]
        ratioY = pygame.display.get_window_size()[1]/screen_size[1]
        size = (self.min_box_size[0], self.min_box_size[1])
        frame = pygame.Surface(size, pygame.SRCALPHA)
        pos = self.pos
        pos = (pos[0] * ratioX, pos[1] * ratioY)

        rect = self.input_rect
        font = self.base_font
        self.base_font = pygame.font.Font(None, int(self.min_box_size[1]))
        ln = len(self.user_text)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                detect_rect = rect
                detect_rect[0] = pos[0]/ratioX
                detect_rect[1] = pos[1]/ratioY
                mouse_pos = (mouse_pos[0]/ratioX, mouse_pos[1]/ratioY)
                if detect_rect.collidepoint(mouse_pos):
                    self.active = True
                else:
                    self.active = False
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and self.active:

                # Check for backspace
                if event.key == pygame.K_BACKSPACE:

                    # get text input from 0 to -1 i.e. end.
                    if self.select_pos < len(self.user_text):
                        self.user_text = self.user_text[:ln - self.select_pos - 1] + self.user_text[ln - self.select_pos:]
                elif event.key == pygame.K_ESCAPE or event.key == pygame.K_KP_ENTER or event.key == 13:
                    self.active = False
                elif event.key == pygame.K_LEFT and self.select_pos < len(self.user_text):
                    self.select_pos += 1
                elif event.key == pygame.K_RIGHT and self.select_pos > 0:
                    self.select_pos -= 1
                elif event.key == pygame.K_DELETE:
                    if self.select_pos > 0:
                        self.user_text = self.user_text[:ln - self.select_pos] + self.user_text[ln - self.select_pos + 1:]
                        self.select_pos -= 1

                else:
                    self.user_text = self.user_text[:ln - self.select_pos] + event.unicode + self.user_text[ln - self.select_pos:]

        if self.active:
            self.color = self.color_active
            self.text_color = self.color_active_text
        else:
            self.color = self.color_passive
            self.text_color = self.color_passive_text


        k = pygame.key.get_pressed()
        k2 = pygame.key.get_mods()

        if self.active:
            if pygame.time.get_ticks() // 500 % 2 == 1:
                if self.select_pos <= 0:
                    text_surface = self.base_font.render(self.user_text + "|", True, self.text_color)
                else:
                    text_surface = self.base_font.render(self.user_text[:ln - self.select_pos] + "|" + self.user_text[ln - self.select_pos:],
                                                    True, self.text_color)
            else:
                text_surface = self.base_font.render(self.user_text, True, (self.text_color))

            if k2 == 4160 and k[pygame.K_BACKSPACE] and k[pygame.K_a] or k2 == 4160 and k[pygame.K_DELETE] and k[
                pygame.K_a]:
                self.user_text = ""
        else:
            if self.user_text == "":
                text_surface = self.base_font.render(self.none_sel_text, True, self.text_color)
            else:
                text_surface = self.base_font.render(self.user_text, True, self.text_color)
        self.input_rect = pygame.Rect(0, 0, text_surface.get_width(), rect[3])
        size = (text_surface.get_width(), rect[3])
        frame = pygame.transform.scale(frame, size)
        pygame.draw.rect(frame, self.color, self.input_rect)
        frame.blit(text_surface, (self.input_rect.x, self.input_rect.y + 5))
        size = (size[0] * ratioX, self.min_box_size[1] * ratioY)
        frame = pygame.transform.scale(frame, size)
        workspace.blit(frame, pos)
        self.input_rect = rect
        self.base_font = font
        self.input_rect.w = max(self.min_box_size[0], text_surface.get_width() + 10)

        return self.user_text


class Slider:
    """sliders are great way to get value in specific range from the user!"""

    def __init__(self, pos: pygame.math.Vector2, size: pygame.math.Vector2, num_min=0, num_max=10,
                 slider_image=None, back_color=(255, 255, 255, 0), slider_color=(0, 0, 0), hover_color=(200, 200, 200),
                 drag_color=(100, 100, 100)):
        if num_max == 0:
            raise ValueError("max slider value can't be 0 or negative number (yet).")
        elif num_max < 0 or num_min < 0:
            raise ValueError("we're not support negative sliders yet.")
        self.pos = pos
        self.size = size
        self.num_min = num_min
        self.num_max = num_max
        # self.step = step
        self.img = slider_image
        self.back_col = back_color
        self.col = slider_color
        self.hov_col = hover_color
        self.drag_col = drag_color
        self.value = num_min
        self.drag = False

    def show(self, workspace: pygame.Surface):
        """put the slider on a surfaced"""
        size = self.size
        pos = self.pos
        if workspace.get_size() != screen_size:
            x = workspace.get_size()[0]
            y = workspace.get_size()[1]
            x = x / screen_size[0]
            y = y / screen_size[1]
            # size = (size[0] * x, size[1] * y)
            # pos = (pos[0] * x, pos[1] * y)

        Draw.draw_rect(workspace, pos, size, self.back_col, size[1])
        col = self.col
        Draw.draw_rect(workspace, (pos[0], pos[1] + (size[1] / 2)), (size[0], size[1] / 8), col, size[1])
        dp = pos[0]
        dp += (size[0]/(self.num_max-self.num_min))*(self.value-self.num_min)
        mp = pygame.mouse.get_pos()
        mp = (mp[0] // x, mp[1] // y)
        mp = (mp[0], mp[1])
        if not pygame.mouse.get_pressed()[0]:
            self.drag = False
        elif pygame.mouse.get_pressed()[0] and not self.drag and not Buttons.click:
            if pos[0] < mp[0] < pos[0]+size[0] and pos[1]-size[1] < mp[1] < pos[1]+size[1]:
                self.drag = True
        if self.drag:
            delta_val = self.num_max-self.num_min
            col = self.drag_col
            nv = ((mp[0]+(size[0]/delta_val))-self.pos[0])/(size[0]/delta_val)
            nv = nv+self.num_min
            nv = max(self.num_min, min(self.num_max, nv))
            nv = int(nv)
            self.value = nv
        elif pos[0] < mp[0] < pos[0]+size[0] and pos[1]-size[1] < mp[1] < pos[1]+size[1]:
            col = self.hov_col
        r = size[1]/2
        Draw.draw_circle(workspace, (dp-r, pos[1]), r, col, int(r*2))

    def change_variables(self, pos=None, size=None, num_min=None, num_max=None,
                         slider_image=0, back_color=None, slider_color=None, hover_color=None, drag_color=None):
        """change the slider initial parameters without create another one"""
        if pos:
            self.pos = pos
        if size:
            self.size = size
        if num_min:
            self.num_min = num_min
        if num_max:
            self.num_max = num_max
        # self.step = step
        if slider_image != 0:
            self.img = slider_image
        if back_color:
            self.back_col = back_color
        if slider_color:
            self.col = slider_color
        if hover_color:
            self.hov_col = hover_color
        if drag_color:
            self.drag_col = drag_color

        self.value = max(min(self.num_min, self.value), self.num_max)
        self.drag = False

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)


class LoadingBar(object):
    """way to visualize percents"""
    def __init__(self, max_num: float, pos: pygame.Vector2, size: pygame.Vector2, color: pygame.Color,
                 back_color: pygame.Color, text_color: pygame.Color, border: int, font='freesansbold.ttf',
                 starting_text=""):
        self.max_num = max_num
        self.pos = pos
        self.size = size
        self.color = color
        self.border = border
        self.value = 0
        self.back_color = back_color
        self.font = font
        self.text = starting_text
        self.text_color = text_color

    def show(self, surf: pygame.Surface):
        """put the loading bar on a surface"""
        text = self.text
        Draw.draw_rect(surf, self.pos, self.size, self.back_color, self.size[0])
        border = self.border
        pos = self.pos
        pos = (pos[0] + border, pos[1] + border)
        size = self.size
        border *= 2
        size = (size[0] - border, size[1] - border)
        loading_size = (size[0] * (self.value / self.max_num), size[1])
        Draw.draw_rect(surf, pos, loading_size, self.color, size[0])
        text += "." * int((time.time() % 3) + 1)
        pos = (int(pos[0] + (size[0] / 2)), int(pos[1] + (size[1] / 2)))
        fast_text(surf, text, size[1] / 2, self.text_color, pos, 1, self.font)

    def change_value(self, value: int, text=""):
        """change current text and value of the loading bar"""
        self.value += value
        self.text = text

    def change_variables(self, max_num=None, pos=None, size=None, color=None, back_color=None, text_color=None,
                         border=None, font=None):
        """change the starting parameters after creating the loading bar (except text. to change the text use:
        change_value(val: int, TEXT: STR))"""
        if max_num:
            self.max_num = max_num
        if pos:
            self.pos = pos
        if size:
            self.size = size
        if color:
            self.color = color
        if border:
            self.border = border
        if back_color:
            self.back_color = back_color
        if font:
            self.font = font
        if text_color:
            self.text_color = text_color


class Tick:
    """"""

    def __init__(self, pos: pygame.Vector2, size: pygame.Vector2, color=(200, 200, 200), hover_color=(100, 100, 100, 100),
                 ticked_color=(0, 255, 150), tick_color=(255, 255, 255)):
        self.value = False
        self.pos = pos
        self.size = size
        self.color = color
        self.hover_color = hover_color
        self.tick_color = tick_color
        self.ticked_color = ticked_color
        self.button = Buttons.Button(pos, size, None, "", tick_color, size[1]*0.8, hover_color=hover_color,
                                     back_color=color)

    def show(self, workspace):
        if self.value:
            self.button.back_color = self.ticked_color
            self.button.text = "X"
        else:
            self.button.back_color = self.color
            self.button.text = ""

        if self.button.is_clicked(workspace):
            self.value = not self.value

        self.button.show(workspace)

    def __bool__(self):
        return self.value

    def __mul__(self, other):
        if self.value:
            n = 1
        else:
            n = 0
        return other*n


