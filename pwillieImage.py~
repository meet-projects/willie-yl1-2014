import pygame
from view import View
class Image (View):
	def __init__(self,_rec, _main_screen,image_r):
		super(Image,self).__init__(_rec, _main_screen)
		self.image_r= image_r
	def draw(self):
		img = pygame.image.load(self.image_r)
		self.main_screen.blit(img,self.rec)
	def clear(self):
		img=pygame.Surface([int(self.rec.width),int(self.rec.height)])
		img.fill((255,255,255))
		main_screen.blit(img,self.rec)

'''if __name__ == "__main__":
	main = pygame.display.set_mode((400,400))
	main.fill((255,255,255))
	c = Image([20,20],main,'download.jpg')
	c.draw()
	while (True):
		ev = pygame.event.poll()
		pygame.display.flip()	'''
