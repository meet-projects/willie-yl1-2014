import pygame
import sys
from button import Button
from pWillieFatOL import fatOL
from pWillieBadassOl import badassOl
from pWillieMusicalOL import musicalOl
from pWillieEinstienOl import einstienOl

#for screen  RETURNATION!!!!

def unReplaciationatorTron():
	global refreshock
	refreshock= refreshok - 1

#For screen DELETIATION!!!!!

def replaciationatorTron():
	global refreshock
	refreshock += 1
	bananator = pygame.Rect(0,0,1000,1000)
	bananatorsurface = pygame.Surface([1000,1000])
	bananatorsurface.fill((255,255,255))
	main_screen.blit(bananatorsurface, bananator )
	someLabel = Button(pygame.Rect(0, 200, 500, 100), "We're currently having technical difficulties, sorry for the inconvenience.", None ,(255,255,255),(35,222,59),None,50,main_screen)
	someLabel.draw()
	buttons= []
	returnButton = Button(pygame.Rect(700,750, 100, 100), "Buy MAOR!!!!!", unReplaciationatorTron ,(255,255,255),(35,222,59),None,50,main_screen)
	returnButton.draw()

	buttons.append(returnButton)


def makeItSmart():
	global shoppingCart
	global price
	global number

	s = einstienOl(1000,"",400,"SURPRISE",69)
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

	s = badassOl(5000,"",400,"shemale",9000)
	price+=s.price
	number+=1

def makeItMusical():
	global shoppingCart
	global price
	global number


	s = musicalOl(400,"",400,"shemale",1000)

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

	

	if refreshock == 0:
		buttons = []
		shoppingCart = []

		title = Button(pygame.Rect(200, 50, 240, 90), "\"Adopt\" an Oompa Loompa!", None, (255,255,255), (11, 201, 90), None, 40, main_screen)
		title.draw()

		#Sexy button
		smartlabel = Button(pygame.Rect(50,100, 150, 150), "Einstien Oompa Loompa - $100.00", None ,(255,255,255),(35,222,59),None,30,main_screen)
		smartlabel.draw()
			
		smartbutton = Button(pygame.Rect(50,150, 250, 200), "", makeItSmart ,(35,41,222),(35,222,59),pygame.image.load('doc-snow-white.jpg'),50,main_screen)
		smartbutton.draw()

		buttons.append(smartbutton)

			#Fat oompa loompa 
		d2 = Button(pygame.Rect(50,425, 150, 150), "Fat Oompa Loompa - $30.00", None ,(255,255,255),(35,222,59),None,30,main_screen)
		d2.draw()
			
		b2 = Button(pygame.Rect(50,475, 250, 200), "", makeItFat ,(35,41,222),(35,222,59),pygame.image.load('Fatoompa.jpg'),50,main_screen)
		b2.draw()
		buttons.append(b2)

		thingsBoughtLabel = Button(pygame.Rect(20, 700, 100, 100), "$0.00",None,(255,255,255),(35,222,59),None,50,main_screen)
		thingsBoughtLabel.draw()

		counterLabel = Button(pygame.Rect(300, 700, 800, 50), "0",None,(255,255,255),(35,222,59),None,50,main_screen)
		counterLabel.draw()
		#buttons.append(b)

		#badass button
		badasslabel = Button(pygame.Rect(450,100, 150, 150), "$uper Oompa Loompa - $5000", None ,(255,255,255),(35,222,59),None,30,main_screen)
		badasslabel.draw()
			
		badassbutton = Button(pygame.Rect(450,150, 250, 200), "", makeItBadass ,(35,41,222),(35,222,59),pygame.image.load('cooloompa.jpg'),50,main_screen)
		badassbutton.draw()

		buttons.append(badassbutton)
		#musical oompaloompa

		Musicallabel = Button(pygame.Rect(450,425, 150, 150), "Musical Oompa Loompa - $2000", None ,(255,255,255),(35,222,59),None,30,main_screen)
		Musicallabel.draw()
			
		Musicalbutton = Button(pygame.Rect(450,475, 250, 200), "", makeItMusical ,(35,41,222),(35,222,59),pygame.image.load('musicoompa.jpg'),50,main_screen)
		Musicalbutton.draw()

		buttons.append(Musicalbutton)

		#button for "done"
			
		donebutton = Button(pygame.Rect(600,750, 100, 100), "Done", replaciationatorTron ,(255,255,255),(35,222,59),None,50,main_screen)
		donebutton.draw()


		buttons.append(donebutton)

		#-

	

	while(True):
		ev = pygame.event.poll()
		if ev.type == pygame.QUIT:
			sys.exit()
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
