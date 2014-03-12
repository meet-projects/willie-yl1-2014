import pygame
import sys
from button import Button

if __name__=="__main__":
	pygame.init()
	infoObject = pygame.display.Info()
	main_screen = pygame.display.set_mode((infoObject.current_w - 100, infoObject.current_h - 100), pygame.FULLSCREEN)
	main_screen.fill((255,255,255))

	b = Button(pygame.Rect(100, 100, 800, 800), "TEAM WILLIE",None,(35,41,222),(35,222,59),None,100,main_screen)
	b.draw()
	while(True):
		pygame.display.flip()
