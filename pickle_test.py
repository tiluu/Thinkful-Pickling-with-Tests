import unittest
from pickler import list_pickler, unpickler

class PicklerTests(unittest.Testcase):
	def setUp(self):
		self.my_list=[1,2,3,4,5,6]
		self.path='./pickle_temp'
		os.makedirs(self.path) #creates a folder
		self.file= os.path.join(self.path, 'list.pk1')
		
	def pickle_list_variable_test(self):
