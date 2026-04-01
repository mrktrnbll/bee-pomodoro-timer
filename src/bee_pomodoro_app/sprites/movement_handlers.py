"""position and movement handlers for sprites"""

def get_random_spawn_position(screen_width, screen_height, sprite_width, sprite_height) -> tuple[int, int]:
    """returns a random position for a sprite to spawn on the screen"""
    import random
    x = random.randint(sprite_width, screen_width - sprite_width)
    y = random.randint(sprite_height, screen_height - sprite_height)
    return x, y

def is_position_populated(self, inserting_x: int, inserting_y: int) -> bool:
    """checks if a position is already populated by another sprite"""
    for position in self.populated_positions:
        position_x, position_y = position[0], position[1]
        if (position_x + 80 > inserting_x > position_x - 80) and (position_y + 80 > inserting_y > position_y - 80):
            return True
    return False

def add_position_to_populated_positions(self, inserting_x: int, inserting_y: int) -> None:
    """adds a position to the list of populated positions"""
    self.populated_positions.append((inserting_x, inserting_y))

def get_unpopulated_spawn_position(self, screen_width: int, screen_height: int, sprite_width: int, sprite_height: int) -> tuple[int, int]:
    """returns a random spawn position that is not already populated"""
    while True:
        x, y = get_random_spawn_position(screen_width, screen_height, sprite_width, sprite_height)
        if not is_position_populated(self, x, y):
            add_position_to_populated_positions(self, x, y)
            return x, y