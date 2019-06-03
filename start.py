import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super(Player, self).__init__()
		self.surf = pygame.Surface((75, 25))
		self.surf.fill((255, 255, 255))
		self.rect = self.surf.get_rect()

	def update(self, pressed_keys):
		if pressed_keys[K_UP]:
			self.rect.move_ip(0, -5)
		if pressed_keys[K_DOWN]:
			self.rect.move_ip(0, 5)
		if pressed_keys[K_LEFT]:
			self.rect.move_ip(-5, 0)
		if pressed_keys[K_RIGHT]:
			self.rect.move_ip(5, 0)

pygame.init()

screen = pygame.display.set_mode((800, 600))

player = Player()

running = True 

while running:
	#for loop through the event queue
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				running = False
		if event.type == QUIT:
			running = False

	pressed_keys = pygame.key.get_pressed()

	player.update(pressed_keys)

	screen.blit(player.surf, player.rect)
	pygame.display.flip()

