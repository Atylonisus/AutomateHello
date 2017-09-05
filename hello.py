#This Program says hello, and asks for my name.

print('Hello world!')
print('What is your name?')		#asks for their name
myName = input()				#a new variable, which will store whatever the user types here
print('It is good to meet you, ' + myName)	#concatenates a string, with your myName variable, to produce a single sentence
print('The length of your name is:')
print(len(myName))				# prints out the number of characters (letters) present in the myName variable
print('What is your age?')		#asks for age!
myAge = input()					#creates a new variable named myAge, which prompts the user to type something
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
""" The above does a lot of little things all at once. It:
								converts whatever value the user put for the variable myAge into an integer
									(input() always returns a string value regardless if numbers were used --> 42 would come out as '42' so int(myAge) would actually make it 42)
								ADDS +1 to that INTEGER value
								Converts the evaluated integer BACK into a string
								and concatenates it into the rest of the sentence, to be printed out to the user
"""
								