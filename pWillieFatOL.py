from pWillieOL import Oompaloompa
class fatOL (Oompaloompa):
	def __init__(self,price,image,height,gender,fatnesslvl):
		super(fatOL,self).__init__(height,gender)
		self.fatnesslvl = fatnesslvl
if __name__ == "__main__":
	c = fatOL(15,13,1,2,2)
	print c.price
	#to do 