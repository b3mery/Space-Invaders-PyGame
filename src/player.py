from pyclbr import Function
import pygame 

import settings

class Player(pygame.sprite.Sprite):
    """Player Class 

    Extends:
        pygame (pygame.sprite.Sprite)
    """
    def __init__(self, groups:list, pos:tuple, generate_attack:Function) -> None:
        super().__init__(groups)
        self.lives = settings.PLAYER_LIVES
        self.image = pygame.image.load('assets/graphics/spaceship.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-10,26)
        
        # Movement
        self.direction = pygame.math.Vector2()
        self.speed = settings.PLAYER_SPEED

        # Attack
        self.generate_attack:Function = generate_attack
        self.can_attack = True
        self.attack_time = None

    def __movement_input(self):
        """Check for movement input. update direction
        """
        keys = pygame.key.get_pressed()
        # Horizontal Inputs
        if keys[settings.RIGHT]:
            self.direction.x += 1
        elif keys[settings.LEFT]:
            self.direction.x += -1
        else:
            self.direction.x = 0
    
    def __attack_input(self):
        """Check for attack input
        """
        keys = pygame.key.get_pressed()
        if keys[settings.ATTACK] and self.can_attack:
            self.can_attack = False
            self.attack_time = pygame.time.get_ticks()
            x = self.rect.centerx -15
            y = self.hitbox.top - 15 
            self.generate_attack((x,y), -1)

    def take_damage(self):
        """Decrease lives
        """
        self.lives -=1

    def __move(self,speed=5):
        """Move the Entity"""
        # Check vector length and normalize
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.__check_horizontal_collisions()
        self.rect.center = self.hitbox.center

    def __check_horizontal_collisions(self) -> None:
        """Check for horizontal collisions. 
        Stop player from going out of bounds
        """
        right_border = pygame.display.get_surface().get_size()[0]
        if self.direction.x < 0 and self.hitbox.left <= 0: # moving left
            self.hitbox.left = 0
        
        if self.direction.x > 0 and self.hitbox.right >= right_border: # moving right
            self.hitbox.right = right_border

    def __cool_down(self):
        """Method for tracking player cooldowns
        """
        current_time = pygame.time.get_ticks()
        # Player Attack Cool Down
        if not self.can_attack and current_time - 700 >= self.attack_time:
            self.can_attack = True

    def update(self) -> None:
        """Public Sprite Update Method
        """
        self.__movement_input()
        self.__attack_input()
        self.__cool_down()
        self.__move(self.speed)