from pWillieOL import Oompaloompa
class fatOL (Oompaloompa):
	def __init__(self,price,image,height,gender,fatnesslvl):
		super(fatOL,self).__init__(price,image,height,gender)
		self.fatnesslvl = fatnesslvl

