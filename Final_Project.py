# Name: Justin Lin & Tilden Jackson
# Date: 11/2/2018
# Description: Final Project ----> Periodic Table Element Table
# Source(s): (https://realpython.com/python-csv/), (https://www.youtube.com/watch?v=q5uM4VKywbA)
import csv

class PeriodicTable:
	def __init__(self):
		self.elements = []
	def main(self):
		d = PeriodicTable()
		print("Hello, I am Chem Bot. If you would like, you can either find the information for a single element or the mass of a compound")
		command = str(input('To find the information for a single element, enter: I,"ElementSymbol"\nTo find the Molar Mass of a compound, enter: M,"Compound"\n'))
		if command[:1].upper() == 'I':
			print(d.Info(str(command[2:])))
		elif command[:1].upper() == 'M':
			print(d.Mass(str(command[2:])))
		else:
			print("You have entered your command incorrectly, please try again!")
			d.main()
	def Info(self, Element):
		import os,csv
		os.chdir(r'C:\Users\tilde\Desktop')
		with open('elements.csv') as csv_file:
			csv_read = csv.reader(csv_file, delimiter=',')
			next(csv_read)
			for line in csv_read:
				if str(Element) == str(line[2]):
					return "\n\n"+str(line[0])+":\n"+"Atomic Number: "+str(line[1])+"\nSymbol: "+str(line[2])+"\nAtomic Mass: "+str(line[3])
	def Mass(self, str_compound):
		d = PeriodicTable()
		mass = 0
		for a in d.SeperateCompound(str_compound):
			mass+=d.MolarMass(str(a))
		return "\nThe Molar Mass of "+str(str_compound)+" is: "+str(mass)
	def MolarMass(self, elsymb):
		import os, csv
		os.chdir(r'C:\Users\tilde\Desktop')
		with open('elements.csv') as csv_file:
			csv_read = csv.reader(csv_file, delimiter=',')
			next(csv_read)
			for line in csv_read:
				if str(elsymb) == str(line[2]):
					return float(line[3])
	def SeperateCompound(self, str_compound):
		compound = [] 
		for a in str_compound:
			compound += [a] # this will store all the characters & digits mentioned in the d.Mass(___) below
		compound+=[0] # this exists to let the code read the end of the string
		i = 0 # The limiter of the while loop below
		while i<len(str_compound)+1: # This will loop through the enitrety of the compound string
			if str(compound[i]).isdigit() == True: # This checks to see if the compound is a digit. 
				e = 1 # This variable will move the checking mechanism for the integers inside 
				if compound[i] == 0 and i == len(str_compound) and str(compound[i-1]).isdigit() == False:
					n = 1
				else:
					n = ''
					while True:
						if i+e<len(str_compound):
							if str(compound[i+e]).isdigit() == True:
								e+=1
							else:
								break
						else:
							break
					for r in range(e):
						n += str(compound[i+r])
				self.elements += [element]*int(n)
				i+=(e-1)
			elif compound[i] == compound[i].upper(): # this will run through when it sees a capilized 
				element = str(compound[i])
				if str(compound[i+1]).isdigit() == False:
					if compound[i+1] == compound[i+1].upper():
						self.elements += [element]
			elif compound[i] == compound[i].lower():
				element += str(compound[i])
				if str(compound[i+1]).isdigit() == False:
					self.elements += [element]
			i+=1
		return self.elements
		print(elements)
	def Balance(self, react1,react2,prod1,prod2):
		d.SeperateCompound()
		return

d = PeriodicTable()
# d.main()
d.SeperateCompound("H2O")
