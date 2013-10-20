from person import Person
from random import randint

class Finder(Person):

	def __init__(self):
		self.coords = (0, 0)
		self.parent = None
		self.children = []

	def move(self, mode):
		
		mv_sz = 2

		if mode == 'rand':
			new_coords = (self.coords[0] + randint(-mv_sz,mv_sz), self.coords[1] + randint(-mv_sz,mv_sz))
			self.coords = new_coords

	def find_zone(self):
		return (self.coords, self.sight_max)

###Tests###

if __name__ == '__main__':

	#Make an empty finder and set its coordinates
	test_finder = Finder()
	assert(test_finder.coords == (0, 0))

	test_finder.coords = (1.0, -1.0)
	assert(test_finder.coords == (1.0, -1.0))

	#Move the finder
	test_finder.move(mode='rand')

	print 'All tests passed.'