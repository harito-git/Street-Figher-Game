#Harit Oza
#January 18, 2022
#Ms. T
#The purpose of this program is to make a 2 player, street fighter game like Tekken with an ancient egyptian theme. This game is a 2 player game, where the player, is the mummy, and the enemy is the minotaur. Both characters are control by various key presses and players.

#import pygame, sys, time, and pygame features

import pygame, sys, time
from replit import audio
from pygame import mixer
from pygame.locals import (
  K_UP,
  K_DOWN,
  K_LEFT,
  K_RIGHT,
  K_ESCAPE,
  K_k,
  K_w,
  K_a,
  K_d,
  K_s,
  KEYUP,
  KEYDOWN,
  QUIT,
)

#set clock and fps of game.
clock = pygame.time.Clock()
fps = 60

#set width fo screen, accceleration and velocity.
WIDTH = 400
acc = 0
vel = 0

#initialize pygame.
pygame.init()

#play audio in repl.it.
source = audio.play_file('mixkit-martial-arts-fast-punch-2047.wav', 80)

#set background of image.
DISPLAYSURF = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption('Background')
image = pygame.image.load("background2.png").convert()
imagesize = (800, 800)
image = pygame.transform.scale(image, imagesize)
DISPLAYSURF.blit(image, (0, 0))
pygame.display.flip()

#load all images into ypgame for player and enemy movement, and attack animations.
global healthbars
h1 = pygame.image.load("heart0.png").convert_alpha()
h2 = pygame.image.load("heart.png").convert_alpha()
h3 = pygame.image.load("heart2.png").convert_alpha()
h4 = pygame.image.load("heart3.png").convert_alpha()
h5 = pygame.image.load("heart4.png").convert_alpha()
h6 = pygame.image.load("heart5.png").convert_alpha()
healthbars = [h1, h2, h3, h4, h5, h6]

r0 = pygame.image.load('Running_000.png').convert_alpha()

r1 = pygame.image.load('Running_001.png').convert_alpha()
r2 = pygame.image.load('Running_002.png').convert_alpha()
r3 = pygame.image.load('Running_003.png').convert_alpha()
r4 = pygame.image.load('Running_004.png').convert_alpha()
r5 = pygame.image.load('Running_005.png').convert_alpha()
r6 = pygame.image.load('Running_006.png').convert_alpha()

a0 = pygame.image.load('Attacking 01_000.png').convert_alpha()
a1 = pygame.image.load('Attacking 01_001.png').convert_alpha()
a2 = pygame.image.load('Attacking 01_002.png').convert_alpha()
a3 = pygame.image.load('Attacking 01_003.png').convert_alpha()
a4 = pygame.image.load('Attacking 01_004.png').convert_alpha()
a5 = pygame.image.load('Attacking 01_005.png').convert_alpha()
a6 = pygame.image.load('Attacking 01_006.png').convert_alpha()
a7 = pygame.image.load('Attacking 01_007.png').convert_alpha()
a8 = pygame.image.load('Attacking 01_008.png').convert_alpha()
a9 = pygame.image.load('Attacking 01_009.png').convert_alpha()
a10 = pygame.image.load('Attacking 01_010.png').convert_alpha()
a11 = pygame.image.load('Attacking 01_011.png').convert_alpha()
a12 = pygame.image.load('Attacking 01_012.png').convert_alpha()

w0 = pygame.image.load('Minotaur_03_Walking_006.png').convert_alpha()
w1 = pygame.image.load('Minotaur_03_Walking_007.png').convert_alpha()
w2 = pygame.image.load('Minotaur_03_Walking_008.png').convert_alpha()
w3 = pygame.image.load('Minotaur_03_Walking_009.png').convert_alpha()
w4 = pygame.image.load('Minotaur_03_Walking_010.png').convert_alpha()
w5 = pygame.image.load('Minotaur_03_Walking_011.png').convert_alpha()
w6 = pygame.image.load('Minotaur_03_Walking_012.png').convert_alpha()
w7 = pygame.image.load('Minotaur_03_Walking_013.png').convert_alpha()
a01 = pygame.image.load('Minotaur_03_Attacking_001.png').convert_alpha()
a02 = pygame.image.load('Minotaur_03_Attacking_008.png').convert_alpha()
a03 = pygame.image.load('Minotaur_03_Attacking_009.png').convert_alpha()


#initialize Player class.
class Player(pygame.sprite.Sprite):

  #declare def() function to initialize player class variables.
  def __init__(self):
    super().__init__()

    #set player image and initialize player class variables.
    self.image = pygame.image.load('Walking_000.png').convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.x = 0
    global x
    x = self.rect.x
    self.rect.y = 400
    self.run = True
    self.attacking = False
    self.moveframe = 0
    self.attackframe = 0
    self.health = 5
    self.dyingframe = 0

    #upload intial health bar heart image with 3 hearts for player.
    self.image2 = pygame.image.load("heart5.png").convert_alpha()
    DISPLAYSURF.blit(self.image2, (0, 0))
    global acc
    global run_animation

    #intialize running animation list.
    run_animation = [r0, r1, r2, r3, r4, r5, r6]

    global attack_animation

    #intialzie attack animation list.
    attack_animation = [a7, a8, a9]

    #set the size of the player mummy character.
    self.x = 300
    self.y = 300
    images = (self.x, self.y)
    self.image = pygame.transform.scale(self.image, images)

#declare function to move player.

  def player_mov(self):

    #conditions to check which key the user presses.
    if pressed_keys[K_a]:
      self.rect.x -= 10
      self.run = True
      global acc
      acc += 1

    if pressed_keys[K_d]:
      self.rect.x += 10
      self.run = True
      acc += 1

    if pressed_keys[K_s]:
      player.attack()

    #conditions to make sure player does not go off the screen.
    if self.rect.left < 0:
      self.rect.left = 0
    if self.rect.right > 1200:
      self.rect.right = 1200

  #declare def() function to update player running animation by going thoroguh the player animation list using if statements.
  def update(self):

    #condition to check if the variable moveframe is greater than 6.
    if self.moveframe > 6:
      self.moveframe = 0
      self.attacking = True
      return

    #condition check if the variable self.run equals true.
    if self.run == True:
      if (self.rect.x > 0 and acc > 0):

        #Loop thorugh player animation list and run the player animation.
        self.image = run_animation[self.moveframe]
        images = (300, 300)
        self.image = pygame.transform.scale(self.image, images)
      self.moveframe += 1

  #def() function for running player attacking animations.
  def attack(self):

    #check if variable self.attackframe is greater than 2.
    if self.attackframe > 2:
      print(self.attackframe)
      self.attackframe = 0

      print(self.attackframe)
      return

    #condition to check if variable self.attacking equals True.
    if self.attacking == True:

      #condition if self.rect.x is greathan 0
      if (self.rect.x > 0):

        #loop through player attacking animations.
        self.image = attack_animation[self.attackframe]
        images = (300, 300)
        self.image = pygame.transform.scale(self.image, images)
      self.attackframe += 1

  #def() function for running player's health bar.
  def player_health(self):

    #condition to check if enemy has hit the player.
    if (pressed_keys[K_k] and player.rect.left >= enemy.rect.left - 20
        and enemy.attackframe == 2):
      time.sleep(0.5)
      self.health = self.health - 1  #decrease health by 1.
      self.image2 = healthbars[self.health]

    #check if player has died, and it's health is less than 0.
    if (self.health <= 0):

      #display minotaur enemy winning image.
      image = pygame.image.load("minotaurwins.png").convert()
      imagesize = (800, 800)
      image = pygame.transform.scale(image, imagesize)
      DISPLAYSURF.blit(image, (0, 0))
      pygame.display.flip()

      #play audio.
      source2 = audio.play_file('mixkit-arcade-retro-game-over-213.wav', 80)
      while True:
        pass

  #update player image after dying.
  def update2(self):
    DISPLAYSURF.blit(self.image2, (0, 0))


#initialize enemy class.
class Enemy(pygame.sprite.Sprite):

  #declare def() function to initialize enemy class variables.
  def __init__(self1):
    super().__init__()

    #set enemy image and initialize variables.
    self1.image = pygame.image.load(
      'Minotaur_03_Walking_005.png').convert_alpha()
    self1.rect = self1.image.get_rect()
    self1.rect.x = 400
    self1.rect.y = 400
    self1.run = True
    self1.attacking = True
    self1.moveframe = 0
    self1.attackframe = 0
    self1.dyingframe = 0
    global y
    y = self1.rect.x
    self1.image = pygame.transform.flip(self1.image, True, False)
    images = (300, 300)
    self1.image = pygame.transform.scale(self1.image, images)
    self1.health = 5

    self1.image2 = pygame.image.load("heart5.png").convert_alpha()

    #store enemy walking animations in a tuple.
    global walk_animation
    walk_animation = (w0, w1, w2, w3, w4, w5, w6, w7)

    #store enemy attack animations in a dictionary.
    global attack_animation2
    attack_animation2 = {0: a01, 1: a02, 2: a03}

  #def() function to move enemy based on which keys are pressed.
  def enemy_mov(self1):

    #conditions to check which keys the user presses.
    if pressed_keys[K_RIGHT]:
      self1.rect.x += 10
      self1.run = True
      global vel
      vel += 1
    if pressed_keys[K_LEFT]:
      self1.rect.x += -10
      self1.run = True
      vel += 1

    if pressed_keys[K_k]:
      enemy.attack()

    #conditions to make sure enemy does not go off the screen.
    if self1.rect.left < 0:
      self1.rect.left = 0
    if self1.rect.right > 1200:
      self1.rect.right = 1200

  def update(self1):

    #condition to check if variable self1.moveframe is greater than 7.
    if self1.moveframe > 7:
      self1.moveframe = 0
      return

    #condition to check if variable self.run is true.
    if self1.run == True:

      #condition to make sure enemy is moving and looping through enemy movement animations.
      if (self1.rect.x > 0 and vel > 0):

        #loop through enemy movement animations.
        self1.image = walk_animation[self1.moveframe]
        self1.image = pygame.transform.flip(self1.image, True, False)
        images = (300, 300)
        self1.image = pygame.transform.scale(self1.image, images)
      self1.moveframe += 1

  #def() function to go through enemy movement animations.
  def attack(self1):

    #condition to check if variable self1.attackframe is greater than 1.
    if self1.attackframe > 1:
      self1.attackframe = 0
      return

    #condition to check if variable self1.attacking equals true.
    if self1.attacking == True:

      #condition to make sure enemy is moving and looping through enemy movement animations.
      if (self1.rect.x > 0):

        #loop through enemy attack animations.
        self1.image = attack_animation2.get(self1.attackframe)
        self1.image = pygame.transform.flip(self1.image, True, False)
        images = (300, 300)
        self1.image = pygame.transform.scale(self1.image, images)
      self1.attackframe += 1

  #def() function to update enemy health.
  def enemy_health(self1):

    #condition to check if enemy is hit by player.
    if (pressed_keys[K_s] and player.rect.left >= enemy.rect.left - 20
        and player.attackframe == 2):
      time.sleep(0.5)
      self1.health = self1.health - 1
      self1.image2 = healthbars[self1.health]  #decrease health by 1.

  #condition to check if enemy has died and health is less than or equal to 0.
    if (self1.health <= 0):

      #display mummy player winning image.
      image = pygame.image.load("mummywins.png").convert()
      imagesize = (800, 800)
      image = pygame.transform.scale(image, imagesize)
      DISPLAYSURF.blit(image, (0, 0))
      pygame.display.flip()

      #play audio.
      source1 = audio.play_file('mixkit-arcade-retro-game-over-213.wav', 80)
      while True:
        pass

  #update enemy image after dying.

  def update2(self1):
    DISPLAYSURF.blit(self1.image2, (400, 0))


enemy = Enemy()
player = Player()

playergroup = pygame.sprite.Group()
playergroup.add(player)
while True:
  clock.tick(30)
  for event in pygame.event.get():
    if event.type == KEYDOWN:
      if event.key == K_k:
        if (player.attacking == True):
          player.attack()
          pygame.display.flip()

        # If the Esc key is pressed, then exit the main loop
      if event.key == K_ESCAPE:
        running = False
    # Check for QUIT event. If QUIT, then set running to false.
    elif event.type == QUIT:
      running = False

    #condition to check if there are no keys being pressed by the user.
    if event.type == KEYUP:
      acc = 0
      vel = 0
  pressed_keys = pygame.key.get_pressed()

  #update screen and call all player class and enemy class functions.
  DISPLAYSURF.fill((0, 0, 0))
  DISPLAYSURF.blit(image, (0, 0))
  player.player_mov()
  enemy.enemy_mov()
  enemy.update()
  player.player_health()
  player.update2()
  enemy.enemy_health()
  enemy.update2()

  player.update()

  #draw the player, the mummy and the enemy, the minotaur onto the screen.
  DISPLAYSURF.blit(enemy.image, enemy.rect)
  DISPLAYSURF.blit(player.image, player.rect)
  pygame.display.flip()
