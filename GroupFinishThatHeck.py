# Name: Justin Lin & Tilden Jackson
# Date: 11/2/2018
# Description: Final Project ----> Periodic Table Element Table
# Source(s): (https://realpython.com/python-csv/), (https://www.youtube.com/watch?v=q5uM4VKywbA), (https://stackoverflow.com/questions/1155617/count-the-number-occurrences-of-a-character-in-a-string)
import csv,os

class PeriodicTable:
	def __init__(self):
		os.chdir(r'C:\Users\tilde\Desktop')
		with open('elements.csv') as csv_file:
			csv_read = csv.reader(csv_file, delimiter=',')
			next(csv_read)
			self.Table = [DataType(line[0],line[2],line[1],line[3]) for line in csv_read]

	def main(self):
		d = PeriodicTable()
		command = input("\nHello this is ChemBot. \nIn order to proceed, enter a compound for the molar mass or an element symbol for the element's information. \nIn order to quit at any time, enter 'quit' or 'exit'\n\n")
		if command.lower() == 'exit' or command.lower() == 'quit':
			print('\n\nThank you for using ChemBot!')
			quit()
		elif len(d.SeperateCompound(str(command))) == 1:
			print(d.Info(str(command)))
			d.main()
		else:
			print(d.Mass(str(command)))
			d.main()

	def Info(self, Element):
		d = PeriodicTable()
		a = self.Table
		for x in range(len(self.Table)+1):
			if x == len(self.Table):
				print("That is an invalid Element Symbol. If you entered a name please try entering a Symbol. (e.x. Hydrogen is H)")
				d.main()
			elif str(a[x].ElementSymbol) == str(Element):
				return "\n\n"+str(a[x].ElementName)+":\n"+"Atomic Number: "+str(a[x].AtomicNumber)+"\nSymbol: "+str(a[x].ElementSymbol)+"\nAtomic Mass: "+str(a[x].Weight)
	def Mass(self, str_compound):
		d = PeriodicTable()
		mass = 0
		for a in d.SeperateCompound(str_compound):
			for i in range(len(self.Table)+1):
				if i == len(self.Table):
					print("That is an invalid compound")
					d.main()
				elif str(self.Table[i].ElementSymbol) == str(a):
					mass_add = float(self.Table[i].Weight)
					break
			mass+=mass_add
		mass = int((mass*100))/100
		return "\nThe Molar Mass of "+str(str_compound)+" is: "+str(mass)+" g/mol"
	def SeperateCompound(self, str_compound):
		compound = [] 
		Elements = []
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
				Elements += [element]*int(n)
				i+=(e-1)
			elif compound[i] == compound[i].upper(): # this will run through when it sees a capitilized 
				element = str(compound[i])
				if str(compound[i+1]).isdigit() == False:
					if compound[i+1] == compound[i+1].upper():
						Elements += [element]
			elif compound[i] == compound[i].lower():
				element += str(compound[i])
				if str(compound[i+1]).isdigit() == False:
					Elements += [element]
			i+=1
		return Elements
	def Balance(self):#, react1,react2,prod1,prod2):
		d = PeriodicTable()
		react1 = "Li"
		react2 = "H3PO4"
		prod1 = "H2"
		prod2 = "Li3PO4"
		print(d.Bal2(react1),d.Bal2(react2),d.Bal2(prod1),d.Bal2(prod2))
	def Bal2(self, react2):
		d = PeriodicTable()
		name = d.SeperateCompound(react2)
		difchars = []
		for x in range(len(name)):
			for a in range(len(difchars)+1):
				if a == len(difchars):
					difchars += [str(name[x])]
				elif name[x] == difchars[a]:
					break
		returned = [[difchars[x],str(name).count(str(difchars[x]))] for x in range(len(difchars))]
		return returned

class DataType():
	def __init__(self,elName,elSymb,Num,Weight):
		self.ElementName = elName
		self.ElementSymbol = elSymb
		self.AtomicNumber = Num
		self.Weight = Weight

	def __str__(self):
		Element = [self.ElementName,self.ElementSymbol,self.AtomicNumber,self.Weight]
		return Element



d = PeriodicTable()
d.main()
# print(d.Balance())
