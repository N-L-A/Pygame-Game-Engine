import types
import pygame
import sys
from PE_tools import Buttons
from PE_tools import gifsPG
from PE_tools import Label
from PE_tools import DataLists
from PE_tools import FolderGifs
from PE_tools import Draw
from PE_tools import sprite
from PE_tools import sound
from PE_tools import maths
from PE_tools import dialogs
from PE_tools import Time
from PE_tools import ImageTransformation
from PE_tools import particles
# from PE_tools import character


PE_version = "ALPHA-1.9.6_(particles&tick-label&scroll&edge-finder&autoFGif_updt)"
clock = pygame.time.Clock()
fps = 0
max_fps = 30
last_events_update = pygame.time.get_ticks()
last_events = []


def init(win_size=(1920, 1080), max_frame_rate=30):
    """initialize pygame and PE
    win_size - the window render resolution
    max_frame_rate - the maximum frame rate"""
    global max_fps
    max_fps = max_frame_rate
    pygame.init()
    Buttons.init(win_size)
    gifsPG.init(win_size)
    Label.init(win_size)
    Draw.init(win_size)
    sprite.init(win_size)
    # character.init(win_size)  # experimental


exit_func = None


def events():
    """put in main loop - this is PE's main tick function
    - get the whole events
    - auto-close window
    - type PE.exit_func = [function] to set the exit function
    - updates the fps clock
    - type PE.fps to get the fps"""
    global fps, last_events_update, last_events
    clock.tick(max_fps)
    fps = clock.get_fps()
    x = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if isinstance(exit_func, types.FunctionType):
                if exit_func() == False:
                    continue
            dialogs.set_cursor_icon(pygame.SYSTEM_CURSOR_ARROW)
            dialogs.root.destroy()
            pygame.quit()
            sys.exit()
        else:
            x.append(event)
    particles.delta_time = delta_time()/100
    last_events_update = pygame.time.get_ticks()
    last_events = x
    return x


def get_fps():
    """get the current FPS
    basically same as PE.clock.get_fps(), but shorter"""
    return clock.get_fps()


def delta_time():
    """get the delta time between last PE.events() call and PE.delta_time() call in milliseconds"""
    return pygame.time.get_ticks()-last_events_update

