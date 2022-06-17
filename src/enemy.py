import pygame

import settings 

class Enemy(pygame.sprite.Sprite):
    """Enemy Class

    Extends:
        pygame (pygame.sprite.Sprite)
    """
    
    def __init__(self, groups:list, pos:tuple ) -> None:
        super().__init__(groups)

        self.image = pygame.image.load('assets/graphics/alien.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(10,26)
        # Movement
        self.direction = pygame.math.Vector2()
        self.speed = settings.ENEMY_SPEED
        self.direction.x = 1

    
    def __move(self,speed=5):
        """Move the Entity"""
        # Check vector length and normalize
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
            
        self.hitbox.x += self.direction.x * speed
        self.rect.center = self.hitbox.center

    @property
    def has_horizontal_collision(self) -> bool:
        """Check if collied on x axis

        Returns:
            bool: True if collied
        """
        right_border = pygame.display.get_surface().get_size()[0]
        if self.direction.x < 0 and self.hitbox.left <= 0: # moving left
            return True
        
        if self.direction.x > 0 and self.hitbox.right >= right_border: # moving right
            return True

        return False

    def take_damage(self):
        """Kill sprite
        """
        self.kill()

    def update(self) -> None:
        """Public update sprite method
        """
        self.__move(self.speed)