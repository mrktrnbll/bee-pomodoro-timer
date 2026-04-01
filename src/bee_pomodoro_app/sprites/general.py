"""
contains functions:
    load_all_sprites(),

"""
import os
import random
from PyQt6.QtGui import QPixmap

def load_sprite(sprite_name: str, image_dir) -> QPixmap:
    """loads a sprite from the assets folder and returns a list of QPixmaps for each frame of the sprite"""
    return QPixmap(os.path.join(image_dir, sprite_name))

def load_random_flower(all_flowers: list[QPixmap]) -> QPixmap:
    """returns a random flower from the list of all flowers"""
    return random.choice(all_flowers)