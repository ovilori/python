#this code loops through a code block by using the while statement
#once roll equals 5, the Boolean expression is False
""" import random

roll = 0
count = 0

while roll != 5:
    count = count + 1
    roll = random.randint(1,5)
    print(roll)

print(f'It took {count} rolls to roll a 5!') """

#using optional statements
#code prompts the user for input i.e name, if the user enters a character, exit the loop
#the first user to roll a 5 wins the game
#perform a gated check on the value entered by the user. If the user enters an empty string, prompts the user to enter a name

import random

roll = 0
count = 0

print('First person to roll a 5 wins!')
while roll != 5:

    name = input('Enter a name, or \'q\' to quit: ')

    if name.strip() == '': # checks if the name variable is empty after removing empty spaces.
        print('You must enter a name to continue')
        continue

    if name == 'q':
        break
    count = count + 1
    roll = random.randint(1,5)
    print(f'{name} rolled {roll}')

else:
    print(f'{name} wins!!!')

print(f'You rolled the dice {count} times.')