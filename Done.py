import pygame
import sys

if __name__=="__main__": 
    pygame.init()
    main_screen = pygame.display.set_mode((800, 800))
    

    label_done = pygame.Rect(50, 50, 200, 30)
    orderlabel = pygame.font.Font(None, 30)
    label = orderlabel.render("You've bought "+ shoppingCart[1]+"Oompa Loompas which cost "+shoppingCart[0]+"$", 1, (0, 0, 0), (255, 255, 255))
    main_screen.blit(label, label_done)


    while True: 
        ev = pygame.event.poll()
        pygame.display.flip()

