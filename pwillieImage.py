import pygame
from view.py import view
class Image (view):
	def __init__(self,_rec, _main_screen,image_r):
		super(Image,self).__init__(_rec, _main_screen)
		self.image_r= image_r
	def draw(self):
		img = pygame.iomage.load(image_r)
		main_screen.blit(image_r,_rec)
		

if __name__ == "__main__":
	main = pygame.display.set_mode((400,400))
	main_screen.fill((255,255,255))
	
	
