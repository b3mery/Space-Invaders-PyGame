import pygame

import settings
from bullet import Bullet
from enemy_controller import Enemies
from player import Player

class Level:
    """Generates and Updates Sprites
    """
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2

        self.visible_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
        self.attackable_sprites = pygame.sprite.Group()

        self.player = Player([self.visible_sprites, self.attackable_sprites], (self.half_width,self.half_height*1.75), self.generate_attack)
        self.enemies = Enemies([self.visible_sprites, self.enemy_sprites, self.attackable_sprites],self.generate_attack)
        self.bullets: list[Bullet] = []

        # main sound
        self.main_sound = pygame.mixer.Sound(open(settings.MAIN_AUDIO_FILE))
        self.main_sound.set_volume(0.5)
        self.main_sound.play(loops=-1)

    
    def generate_attack(self, pos:tuple, direction:int):
        """Generate a bullet attack

        Args:
            pos (tuple): x,y pos
            direction (int): 1 or -1 
            speed (int): speed of bullet
        """
        self.bullets.append(
            Bullet([self.visible_sprites], pos, direction, self.attackable_sprites, self.enemies)
        )
        
    @property
    def is_game_over(self) -> bool:
        """Check if game is over

        Returns:
            bool: True if game is over, else False
        """
        if self.player.lives == 0: 
            return True
        if len(self.enemies.active_enemies) == 0: 
            return True
        if self.enemies.closest_enemy_pos[1] >= self.player.rect.centery:
            return True
        return False

    def run(self):
        """Run the game
        """
        self.visible_sprites.draw(self.display_surface)
        if not self.is_game_over:
            self.enemies.update()
            self.visible_sprites.update()
        else:
            self.main_sound.stop()

