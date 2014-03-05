import pygame
import sys

class View(object):
	def __init__(self,_rec, _main_screen):
		self.isCleared = False
		self.rec = _rec
		self.main_screen = _main_screen
	def draw(self):
		view_rec = pygame.Surface([int(self.rec.width),int(self.rec.height)])
		self.main_screen.blit(view_rec,self.rec)
	def clear(self):
		view_rec = pygame.Surface([int(self.rec.width),int(self.rec.height)])
		view_rec.fill((255,255,255))
		self.main_screen.blit(view_rec,self.rec)
		self.isCleared = True



