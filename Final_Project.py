# Name: Justin Lin & Tilden Jackson
# Date: 11/2/2018
# Description: Final Project ----> Periodic Table Element Table
# Source(s): 

# Name: Justin Lin & Tilden Jackson
# Date: 11/2/2018
# Description: Final Project ----> Periodic Table Element Table
# Source(s): (https://realpython.com/python-csv/), ()

''
""

import csv

class PeriodicTable:
	def __init__(self):
		self.elements = []
		# with open('elements.csv') as csv_file:
		# csv_reader = csv.reader(csv_file, delimiter=',')
	def Mass(self, str_compound):
		compound = []
		for a in str_compound:
			compound += [a]
		compound += [0]
		i = 0
		while i<len(str_compound)+1:
			if str(compound[i]).isdigit() == True:
				if compound[i] == 0 and i == len(str_compound) and str(compound[i-1]).isdigit() == False:
					n = 1
				else:
					n = ''
					e = 1
					while True:
						if i+e<=len(str_compound):
							if str(compound[i+e]).isdigit() == True and (i+e)!=len(str_compound):
								e+=1
							else:
								break
						else:
							break
					for r in range(e):
						n += str(compound[i+r])
				self.elements += [element]*int(n)
				i+=(e-1)
			elif compound[i] == compound[i].upper():
				element = str(compound[i])
				if str(compound[i+1]).isdigit() == False:
					if compound[i+1] == compound[i+1].upper():
						self.elements += [element]
			elif compound[i] == compound[i].lower():
				element += str(compound[i])
				if str(compound[i+1]).isdigit() == False:
					self.elements += [element]
			i+=1
		print(self.elements)
		#add up values by taking value from csv. Then return val

d = PeriodicTable()
d.Mass('HCa102O13')
