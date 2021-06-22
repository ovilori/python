#this program uses the for statement to iterate through a list
#test a value for inclusion in a list

""" numbers = [1, 3, 4, 5]

print(3 in numbers)
print(8 in numbers)

print(3 not in numbers)
print(8 not in numbers)
print('\n') """

#looping through a list using the for keyword
#this will contain the variable name that will hold the next item in the list,
#the in keyword, variable name of the list and the colon symbol to end the statement.
#the code below prints each item in the list cities, one item per line

""" cities = ['New York', 'Paris', 'Chicago', 'London']
#for each item in cities
for city in cities:
    print(city) """

#breaking out of a for loop with break
""" print('\n') #to give a line break from the previous output
number = [4, 30, 35, 65, 42, 1, 16, 23, 5, 55]
number.sort()
for num in number:
    if num > 42:
        break
    print(num) """

#using an else statement
#the program below executes only after each item in the list has been processed.
#it will print 'No numbers greater than 90' only if each number in the random list of five numbers is below the value 90.

""" import random
numbers = []

while len(numbers) < 5:
    numbers.append(random.randint(1,100))

for number in numbers:
    print(number)
    if number >= 90:
        print('Found at least one number greater than 90')
        break
else:
    print('No numbers greater than 90')
print('Complete') """

#this program uses the continue statement in a code block to skip the remaining logic 
#and move to the next item in a list in a for statement.
#the program creates new list that contains only str values from the existing list 

""" values = ['computer', 5, 'washing machine', 6, 'blender', 8]
equipment = []

for value in values:
    if isinstance(value,str) == False:
        continue
    equipment.append(value)
#print the entire array of filtered values
print(equipment)
#to print the output without the [] or ''
print(*equipment, sep=', ')  """

#nested for loops
#nesting a for loop in another for loop helps to generate a combination of values
#this program creates one card for each combination of suits and ranks

""" suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds', ]
ranks = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']

#for each item in suits. Variable holding the item is 'suit'
for suit in suits: 
    #for each item in ranks. Variable holding the item is 'rank'
    for rank in ranks:
        print(f'{rank} of {suit}') """

#choosing randomly from a list
#use the random module to select an item from a list by calling the choice() function
#use the random module to select a number of items from a list by calling the choices() function.

import random
numbers = [42, 77, 16, 101, 23, 8, 4, 15, 55]
#select an iteam from the list
selected_number = random.choice(numbers)
print(selected_number, '\n')
selected_numbers = random.choices(numbers, k=3) #k=3 specifies that we want to select three random numbers.
print(selected_numbers)






