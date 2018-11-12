# Name: Justin Lin & Tilden Jackson
# Date: 11/2/2018
# Description: Final Project ----> Periodic Table Element Table
# Source(s): (https://realpython.com/python-csv/), (https://www.youtube.com/watch?v=q5uM4VKywbA), (https://stackoverflow.com/questions/1155617/count-the-number-occurrences-of-a-character-in-a-string)
# On my honor, I have niether given nor received unauthorized aid.
import csv

class PeriodicTable:
	def __init__(self):
		with open('elements.csv') as csv_file: # this opens the comma-seperated value file
			csv_read = csv.reader(csv_file, delimiter=',') #this lets the program read the csv file
			next(csv_read) #skips the header (element ,number, symbol,  weight, and etc)
			self.Table = [DataType(line[0],line[2],line[1],line[3]) for line in csv_read] #this is to activate the datatype function, using the csv file as the input.

	def main(self):
		d = PeriodicTable() # allows the d variable to activate the class
		command = input("\nHello this is ChemBot. \nIn order to proceed, enter a compound for the molar mass or an element symbol for the element's information. \nIn order to quit at any time, enter 'quit' or 'exit'\n\n") #this is an input for the user to use
		if command.lower() == 'exit' or command.lower() == 'quit': #this is the quiting part of the code.
			print('\n\nThank you for using ChemBot!')
			quit()
		elif len(d.SeperateCompound(str(command))) == 1:
			print(d.Info(str(command)))
			d.main()
		else:
			print(d.Mass(str(command)))
			d.main()

	def Info(self, Element):
		d = PeriodicTable() # allows the d variable to activate the class
		a = self.Table # this contains the csv
		for x in range(len(self.Table)+1):
			if x == len(self.Table): # this tells you if inputted a wrong element
				print("That is an invalid Element Symbol. If you entered a name please try entering a Symbol. (e.x. Hydrogen is H)")
				d.main() # sends you back to the start, if wrong element is inputted.
			elif str(a[x].ElementSymbol) == str(Element):
				return "\n\n"+str(a[x].ElementName)+":\n"+"Atomic Number: "+str(a[x].AtomicNumber)+"\nSymbol: "+str(a[x].ElementSymbol)+"\nAtomic Mass: "+str(a[x].Weight) # returns the information on the element
	def Mass(self, str_compound):
		d = PeriodicTable()
		mass = 0
		for a in d.SeperateCompound(str_compound):
			for i in range(len(self.Table)+1):
				if i == len(self.Table): # the program checks if a wrong compound is inputted.
					print("That is an invalid compound")
					d.main() # sends you back to the start.
				elif str(self.Table[i].ElementSymbol) == str(a):
					mass_add = float(self.Table[i].Weight) # a variable that stores the information of the compound’s weight
					Break # breaks the for loop when mass_add has the information.
			mass+=mass_add
		mass = int((mass*100))/100
		return "\nThe Molar Mass of "+str(str_compound)+" is: "+str(mass)+" g/mol" # returns the mass of the compound.
	def SeperateCompound(self, str_compound): # this function is to seperate a compound
		compound = []
		Elements = []
		for a in str_compound:
			compound += [a] # this will store all the characters & digits mentioned in the d.Mass(___) below
		compound+=[0] # this exists to let the code read the end of the string
		i = 0 # The limiter of the while loop below
		element = '' # empty string
		while i<len(str_compound)+1: # This will loop through the enitrety of the compound string
			if str(compound[i]).isdigit() == True: # This checks to see if the compound is a digit. 
				e = 1 # This variable will move the checking mechanism for the integers inside 
				if compound[i] == 0 and i == len(str_compound) and str(compound[i-1]).isdigit() == False: # this is to let the programm know that this is the end of the string
					n = 1 # amount to multiply a element for the compound.
				else:
					n = ''
					while True:
						if i+e<len(str_compound): 
							if str(compound[i+e]).isdigit() == True:
								e+=1 # this is to stop the if statement once e reaches a certain number
							else:
								break
						else:
							break
					for r in range(e):
						n += str(compound[i+r])
				Elements += [element]*int(n) # this will give however many element symbols that was inputted in in the main() function
				i+=(e-1)
			elif compound[i] == compound[i].upper(): # this will run through when it sees a capitilized 
				element = str(compound[i])
				if str(compound[i+1]).isdigit() == False:
					if compound[i+1] == compound[i+1].upper():
						Elements += [element]
			elif compound[i] == compound[i].lower(): # this is to check if it is actually a element symbol or just part of one. (since some symbols can have a lower cased letter after an upper cased one)
				element += str(compound[i])
				if str(compound[i+1]).isdigit() == False:
					Elements += [element] # this is to check if the element is just the 1 element, since having no number after an element is just saying it is 1
			i+=1
		return Elements # returns the entirety of the element.

class DataType(): 
	def __init__(self,elName,elSymb,Num,Weight): # these inputs are all from the csv file from the main() function in the periodic table class
		self.ElementName = elName
		self.ElementSymbol = elSymb
		self.AtomicNumber = Num
		self.Weight = Weight

	def __str__(self): # returns the information of the csv file
		Element = [self.ElementName,self.ElementSymbol,self.AtomicNumber,self.Weight]
		return Element



d = PeriodicTable()
d.main()
