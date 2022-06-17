import pygame

GAME_TITLE = 'Space Invaders'

############################################### Game Setup #####################################################################
WIDTH    = 1280
HEIGHT   = 720
FPS      = 60
BG_COLOUR =  '#2d2e2d'

############################################### User Input  ######################################################################
LEFT = pygame.K_LEFT
RIGHT = pygame.K_RIGHT
ATTACK = pygame.K_SPACE

############################################### Entity Bases  ######################################################################
PLAYER_LIVES = 3
PLAYER_SPEED = 3
ENEMY_SPEED = 1
BULLET_SPEED = 5


############################################### Audio #############################################################################
MAIN_AUDIO_FILE = 'assets/audio/background.wav'
BULLET_AUDIO = 'assets/audio/bullet.wav'
EXPLOSION_AUDIO = 'assets/audio/explosion.wav'
