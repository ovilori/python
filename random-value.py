#this exercise will use an mport statement to utilize a standard library module
#the program below uses the random module to generate a random value.

#import random #importing the random module from the Python standard library
import random as alias #create an alias for the random module
#roll = random.randint(1,10)
roll = alias.randint(1,10)
print(f'you rolled {roll}.')