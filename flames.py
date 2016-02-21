#Flames Calculator
result = {
			'f':"Friendzoned (Friend)",
			'l':"You Have Found the One (Lover)",
			'a':"You Might Hit Things Off (Affair)",
			'm':"You Lucky Bastard (Marriage)",
			'e':"Better Keep a Distance (Enemy)",
			's':"Sister (Self Explanatory)"
		 };
def inp():
	"""
	A function in which the user enters his/her name and her's/his's
	crush's name. The function makes sure that the names consists of
	alphabets only, and if successful returns the names.
	"""
	while True:
		name1 = raw_input("Enter Your Name\n>")
		name2 = raw_input("Enter Your Crush's Name\n>")
		name1 = name1.lower()			
		name2 = name2.lower()
		name1 = name1.replace(" ","")
		name2 = name2.replace(" ","")
		if name1 != name2 and name1.isalpha() and name2.isalpha():      
			break
		else:
			print "Invalid Input!!\n\n"
	return name1,name2

def calc():
	"""
	The function calls the input function and begins to iterate
	over a name. If any character is a match in both the names, then
	it is removed from both the names. Finally the total number of
	dissimilar characters are counted, the flames string is shortened
	according to the rules of the game and after exception handling
	the final character from "flames" is returned.
	"""
	flames = "flames"
	name1,name2 = inp()													 
	
	for c in name1:														
		if c in name2: 													
			name1 = name1.replace(c,"",1)								
			name2 = name2.replace(c,"",1)
	length = len(name1) + len(name2)									
	while len(flames)!=1:
		if length%len(flames) == 0:										
			flames  = flames[:len(flames)-1]
		else:
			x = length%len(flames)
			flames = flames[x:] + flames[:x-1]							
	print 
	return flames

def display():
	"""
	The function call the calc() function and matches the returned
	value with the index of the result dictionary and displays the 
	final answer of the game.
	"""
	print result[calc()]												

display()	
