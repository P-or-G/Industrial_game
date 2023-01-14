import os
import sys
from main import *

import pygame

pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
image = load_image("mill_1.png")


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image
