"""position and movement handlers for sprites"""

def get_random_spawn_position(screen_width, screen_height, sprite_width, sprite_height):
    """returns a random position for a sprite to spawn on the screen"""
    import random
    x = random.randint(sprite_width, screen_width - sprite_width)
    y = random.randint(sprite_height, screen_height - sprite_height)
    return x, y