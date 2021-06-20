#this program uses the isnumeric() function to determine if a value entered by the user 
#can be converted to a numeric value for a mathematical operation
#isnumeric() function returns a Boolean value if the string value can be converted into a numeric value.
#step 1 - check the user input to see whether it can be converted into an int
#step 2 - if it can be converted, go ahead and convert it

""" numeric_value = '7'
print (numeric_value.isnumeric())

string_value = 'Olamide'
print(string_value.isnumeric()) """

#this program gate the keyboard input using an if statement and isnumeric() function

""" first_value = input('First number: ')

if first_value.isnumeric() == False:
    print('Value is not a number.')
    exit()

second_value = input('Second number: ')

if second_value.isnumeric() == False:
    print('Value is not a number.')
    exit()

first_value = int(first_value)
second_value = int(second_value)

sum = first_value + second_value
print('Sum: ' + str(sum)) """

first_value = input('Enter first number: ')
second_value = input('Enter second number: ')

if first_value.isnumeric() == False or second_value.isnumeric() == False:
    print('Please, enter only numeric value. Closing...')
    exit()

first_value = int(first_value)
second_value = int(second_value)

sum = first_value + second_value
print('Sum: ' + str(sum))




#same program above using an 'or' operator
