from pWillie import Item
class Oompaloompa(Item):
	def __init__(self,price,image,height,gender):
		super(Oompaloompa, self).__init__(price,image)
		self.height=height
		self.gender=gender

