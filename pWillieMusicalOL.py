from pWillieOL import Oompaloompa
class musicalOl (Oompaloompa):
	def __init__(self,price,image,height,gender,genre):
		super(musicalOl,self).__init__(price,image,height,gender)
		self.genre = genre

