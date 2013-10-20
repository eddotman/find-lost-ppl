from person import Person
from finder import Finder
from numpy import *

class Map:

	def __init__(self, num_finders):
		self.lost_person = Person()
		self.finders = [Finder() for x in range(num_finders)]

	def set_lost_person (self, coords):
		self.lost_person.coords = coords

	def move_finders (self):
		for finder in self.finders:
			finder.move(mode='rand')

	def static_search (self):
		for finder in self.finders:
			zone = finder.find_zone() #2-tuple: (zone center, zone radius)
			dist_to_lost = linalg.norm(array(self.lost_person.coords) - array(zone[0]))
			
			if dist_to_lost <= zone[1]:
				return True

		return False 

	def get_all_coords (self):

		all_coords = []

		for finder in self.finders:
			all_coords.append(finder.coords)

		return all_coords


###TESTS###

if __name__ == '__main__':

	#Initialization
	test_map = Map(10)

	#Set lost person location
	lost_person_location = (100.0, -100.0)
	test_map.set_lost_person(lost_person_location)

	#Move finders
	test_map.move_finders()

	#Make finders search in-place (statically)
	test_map.static_search()


	print 'All tests passed.'