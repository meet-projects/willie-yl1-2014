import pygame
import sys
from view import View
class Button(View):
	def __init__(self,_rec, _text,_action, _color,_textColor, _image, _fontSize, _main_screen):
		super(Button, self).__init__(_rec, _main_screen)
		self.text = _text
		self.action = _action
		self.color = _color
		self.image = _image
		self.textColor = _textColor
		self.thefont = pygame.font.Font(None, _fontSize)
	def draw(self):
		view_rec = pygame.Surface([int(self.rec.width),int(self.rec.height)])
		if self.image is None:
			view_rec.fill(self.color)
		
			#TODO 
		#TODO set background to main screen background
		labelText = self.thefont.render(self.text,1,self.textColor,self.color)
		self.main_screen.blit(view_rec, self.rec)
		self.main_screen.blit(labelText,self.rec)
	def clear(self):
		view_rec = pygame.Surface([int(self.rec.width),int(self.rec.height)])
		view_rec.fill((255,255,255))
		self.main_screen.blit(view_rec,self.rec)
		self.isCleared = True
	def checkIfPosIsInRec(self, x,y):
		if x > self.rec.x and x < (self.rec.x + self.rec.width) and y > self.rec.y and y < (self.rec.y + self.rec.height):
			return True
		else:
			return False
	def updateText(self, text):
		self.clear()
		self.text = text
		self.draw()