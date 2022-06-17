import pygame
import settings
from enemy import Enemy
from enemy_controller import Enemies 

class Bullet(pygame.sprite.Sprite):
    """_summary_

    Args:
        pygame (_type_): _description_
    """
    
    def __init__(self, groups:list, pos:tuple, direction:int, attackable_sprites, enemies ) -> None:
        super().__init__(groups)
        if direction == 1:
            file_name = 'bullet_down'
        else:
            file_name = 'bullet_up'
        self.image = pygame.image.load(f'assets/graphics/{file_name}.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-10,-26)
        
        self.enemies: Enemies = enemies
        self.attackable_sprites = attackable_sprites
        
        # Movement
        self.direction = pygame.math.Vector2()
        self.speed = settings.BULLET_SPEED
        self.direction.y = direction

        pygame.mixer.Sound(settings.BULLET_AUDIO).play()
        self.explode = pygame.mixer.Sound(settings.EXPLOSION_AUDIO)

    def move(self,speed=5):
        """Move the Entity"""
        # Check vector length and normalize
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
            
        self.hitbox.y += self.direction.y * speed
        self.rect.center = self.hitbox.center

    def check_collisions(self):
        """Check for collisons on attackable sprites and out of bounds
        """
        for sprite in self.attackable_sprites:
            if self.rect.colliderect(sprite.rect):
                if isinstance(sprite, Enemy):
                    self.enemies.active_enemies.remove(sprite)
                sprite.take_damage()
                self.explode.play()
                self.kill()

        if self.hitbox.top <= 0 or self.hitbox.bottom >= pygame.display.get_surface().get_size()[1]:
            self.kill()
            

    def update(self) -> None:
        self.move(self.speed)
        self.check_collisions()