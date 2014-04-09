import pygame
import sys
from button import Button
from pWillieShexyOl import ShexyOl
from pWillieFatOL import fatOL
from pWillieBadassOl import badassOl

#For screen DELETIATION!!!!!

def replaciationatorTron():
	global refreshock
	refreshock += 1
	bananator = pygame.Rect(0,0,1000,1000)
	bananatorsurface = pygame.Surface([1000,1000])
	bananatorsurface.fill((255,255,255))
	main_screen.blit(bananatorsurface, bananator )
	someLabel = Button(pygame.Rect(20, 500, 500, 100), "YOU JUST GOT SCAMMED! Thanks for the money!!!!.", None ,(255,255,255),(35,222,59),None,50,main_screen)
	someLabel.draw()
def makeItSexy():
	global shoppingCart
	global price
	global number

	s = ShexyOl(100,"",400,"SURPRISE",69)
	price+=s.price
	number+=1
def makeItFat():
	global shoppingCart
	global number
	global price

	s = fatOL(30,"",400,"SURPRISE",5)
	price+=s.price
	number+=1
	shoppingCart.append(s)

def makeItBadass():
	global shoppingCart
	global price
	global number

	s = badassOl(1000,"",400,"shemale",9000)
	price+=s.price
	number+=1
def makeItMusical():

	global shoppingCart
	global price
	global number

	s = MusicalOl(400,"",400,"shemale",1000)
	price+=s.price
	number+=1

if __name__=="__main__":
	global shoppingCart
	global number
	global price
	global refreshock
	refreshock = 0
	price = 0
	number = 0
	pygame.init()


	infoObject = pygame.display.Info()
	main_screen = pygame.display.set_mode((1000, 1000))
	main_screen.fill((255,255,255))


	buttons = []
	shoppingCart = []

	title = Button(pygame.Rect(200, 50, 240, 90), "\"Adopt\" an Oompa Loompa!", None, (255,255,255), (11, 201, 90), None, 40, main_screen)
	title.draw()

	#Sexy button
	sexylabel = Button(pygame.Rect(50,100, 150, 150), "Sexy Oompa Loompa - $100.00", None ,(255,255,255),(35,222,59),None,30,main_screen)
	sexylabel.draw()
	
	sexybutton = Button(pygame.Rect(50,150, 250, 200), "", makeItSexy ,(35,41,222),(35,222,59),None,50,main_screen)
	sexybutton.draw()

	buttons.append(sexybutton)

	#Fat oompa loompa 
	d2 = Button(pygame.Rect(50,425, 150, 150), "Fat Oompa Loompa - $30.00", None ,(255,255,255),(35,222,59),None,30,main_screen)
	d2.draw()
	
	b2 = Button(pygame.Rect(50,475, 250, 200), "", makeItFat ,(35,41,222),(35,222,59),None,50,main_screen)
	b2.draw()
	buttons.append(b2)

	thingsBoughtLabel = Button(pygame.Rect(20, 700, 100, 100), "$0.00",None,(255,255,255),(35,222,59),None,50,main_screen)
	thingsBoughtLabel.draw()

	counterLabel = Button(pygame.Rect(300, 700, 800, 50), "0",None,(255,255,255),(35,222,59),None,50,main_screen)
	counterLabel.draw()
	#buttons.append(b)

	#badass button
	badasslabel = Button(pygame.Rect(450,100, 150, 150), "Bada$$ Oompa Loompa - $1000", None ,(255,255,255),(35,222,59),None,30,main_screen)
	badasslabel.draw()
	
	badassbutton = Button(pygame.Rect(450,150, 250, 200), "", makeItBadass ,(35,41,222),(35,222,59),None,50,main_screen)
	badassbutton.draw()

	buttons.append(badassbutton)

	Musicallabel = Button(pygame.Rect(450,425, 150, 150), "Musical Oompa Loompa - $2000", None ,(255,255,255),(35,222,59),None,30,main_screen)
	Musicallabel.draw()
	
	Musicalbutton = Button(pygame.Rect(450,475, 250, 200), "", makeItMusical ,(35,41,222),(35,222,59),None,50,main_screen)
	Musicalbutton.draw()

	#button for "done"
	
	donebutton = Button(pygame.Rect(600,750, 100, 100), "Done", replaciationatorTron ,(255,255,255),(35,222,59),None,50,main_screen)
	donebutton.draw()

	buttons.append(donebutton)


	

	while(True):
		ev = pygame.event.poll()
		if ev.type == pygame.QUIT: 
			sys.exit()
		if refreshock == 0:
			if ev.type == pygame.MOUSEBUTTONDOWN:
				x, y = ev.pos
				for button in buttons:
					if button.checkIfPosIsInRec(x,y):
						button.action()
		if number <= 1:
			counterLabel.updateText(str(number) + " Oompa Loompa- BUY MORE!")
		else:
			counterLabel.updateText(str(number) + " Oompa Loompas")


		thingsBoughtLabel.clear()
		thingsBoughtLabel.updateText("$"+str(price))
		pygame.display.flip()
