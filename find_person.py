from map import Map
from numpy import *
import matplotlib.pyplot as plt 

class Person_Finder:

	def __init__(self, num_finders, lost_p_coords):
		
		self.map = Map(num_finders)
		self.map.set_lost_person(lost_p_coords)

		self.is_found = False
		self.coord_list = []


	def iter_find(self):

		while(self.is_found == False):

			if self.coord_list == []:
				self.coord_list = self.map.get_all_coords()
			else:
				self.coord_list = vstack((self.coord_list, self.map.get_all_coords()))

			self.is_found = self.map.static_search()
			self.map.move_finders()



if __name__ == '__main__':

	num_finders = 3
	lost_coords = (50, 50)
	pf = Person_Finder(num_finders, lost_coords)

	pf.iter_find()

	#plot trajectories
	for x in range(num_finders):
		plt.plot(pf.coord_list[x::num_finders, 0], pf.coord_list[x::num_finders, 1])

	#plot beginning and endpoints
		plt.scatter(0.0, 0.0, c='k')
		plt.scatter(pf.map.lost_person.coords[0], pf.map.lost_person.coords[1], c='r')
	
	plt.show()