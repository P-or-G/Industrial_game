import os
import sys
import pygame
import random

# - Window options
TRUE_SIZE = T_W, T_H = 1920, 1024
SIZE = WIDTH, HEIGHT = 1024, 1024
CELL_SIDE = 16
CELL_VERT_NUM = HEIGHT // CELL_SIDE
CELL_HOR_NUM = WIDTH // CELL_SIDE
FPS = 60

# - Sprites options
ass_cell_y_crds = ['grass_1.png', 'grass_2.png', 'grass_3.png', 'grass_4.png', 'rock_1.png', 'rock_2.png', 'rock_3.png',
                                                                                                         'iron.png']
safe_types = ['grass_1.png', 'grass_2.png', 'grass_3.png', 'grass_4.png']

sawmill_types = ['sawmill_1.png', 'sawmill_2.png']

rock_types = ['rock_1.png', 'rock_2.png', 'rock_3.png']

fertile_soils = ['f_s1.png', 'f_s2.png']

# - Gameplay options
start_money = 100
start_wood = 50
start_stone = 25
start_iron = 10
start_bread = 100


# - Useful functions
def load_image(name, colorkey=None):
    fullname = os.path.join('assets', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image
