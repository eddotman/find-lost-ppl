class Person:
	
	coords = ()
	sight_max = 10 #metres

	def __init__(self):
		self.coords = (0, 0)

###Tests###

if __name__ == '__main__':

	#Make an empty person and set its coordinates
	test_person = Person()
	assert(test_person.coords == (0, 0))

	test_person.coords = (1.0, 1.0)
	assert(test_person.coords == (1.0, 1.0))

	print 'All tests passed.'