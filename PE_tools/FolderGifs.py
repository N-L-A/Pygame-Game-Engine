import pygame.image, os
from PE_tools import gifsPG


def gif_from_folder(folder_dir: str, length: int, start=0, format=".png", name="", zero_c=0,
                 pos=(0, 0), size=(100, 100), fps=30, color=(0, 0, 0, 0), rot=0):
    """take lots of images from a folder and turn them into PE gif"""
    img = []
    for i in range(start, length + 1, 1):
        ii = zero_c - len(str(i))
        img.append(pygame.image.load(folder_dir + name + "0" * ii + str(i) + format))
    return gifsPG.Gif(img, pos, size, fps, color, rot)


def auto_gif_from_folder(folder_dir: str, image_format='', name='', pos=(0, 0), size=(100, 100), fps=30, color=(0, 0, 0, 0),
                         rot=0):
    """loads all the images from a folder as a gif.
    set image_format to '' to get all the formats"""
    folder = os.listdir(folder_dir)
    images = []
    for file in folder:
        if file.endswith(image_format) and file.startswith(name):
            images.append(pygame.image.load(folder_dir+file))

    return gifsPG.Gif(images, pos, size, fps, color, rot)
