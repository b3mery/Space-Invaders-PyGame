from pyclbr import Function
from random import randint, choice
import pygame
from enemy import Enemy

class Enemies:
    """Controll Generation and collisions of enemies
    """

    def __init__(self, groups:list, generate_attack:Function) -> None:
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2

        self.sprite_groups = groups
        self.active_enemies: list[Enemy] = []

        self.__generate_enemies()

        self.generate_attack:Function = generate_attack

    def __generate_enemies(self):
        """Generate all enemies
        """
        y_start = 0
        for _ in range(5):
            self.__generate_enemies_row(y_start)
            y_start += 64

    def __generate_enemies_row(self, y_start):
        """Generate a row of enemies

        Args:
            y_start (int): y pos
        """
        x_start = self.half_width * 0.5
        for _ in range(10):
            self.active_enemies.append(
                Enemy(self.sprite_groups, (x_start,y_start))
            )
            x_start += 64
    
    @property
    def has_collision(self) -> bool:
        """Check if an Enemy has collied on x axis

        Returns:
            bool: True is collied
        """
        for enemy in self.active_enemies:
            if enemy.has_horizontal_collision:
                return True
    
    @property
    def closest_enemy_pos(self)-> tuple:
        """Return closest enemy postion on y axis and random x position

        Returns:
            tuple: (x,y)
        """
        closets_y = 0
        for enemy in self.active_enemies:
            if enemy.hitbox.bottom > closets_y:
                closets_y = enemy.hitbox.bottom
        x = choice(self.active_enemies).rect.centerx
        return (x,closets_y)

    def __shoot(self):
        """Randomly generate an attack
        """
        if randint(1,100) == 2:
            x, y = self.closest_enemy_pos
            y += 5
            self.generate_attack((x,y), 1)

    def __switch_direction_and_move_forward(self):
        """* switch direction horizontally
        * move forward on y axis
        * increase speed
        """
        if self.has_collision:
            for enemy in self.active_enemies:
                # Reverse horizontal 
                if enemy.direction.x > 0:
                    enemy.direction.x = -1
                else: 
                    enemy.direction.x = 1 
                enemy.speed += 0.5
                # progress forward
                enemy.hitbox.bottom += 32
                enemy.rect.center = enemy.hitbox.center

    def update(self):
        self.__switch_direction_and_move_forward()
        self.__shoot()