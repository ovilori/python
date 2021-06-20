#program to build a simple calculator
#prompts users for two values and a mathematical operation
#performs the calculation, and then formats and displays the output.

print('SIMPLE CALCULATOR')

first_number = input('First number: ')

if first_number.isnumeric() == False:
    print('Please input a number. Closing the calculator!')
    exit ()

operator = input('Operator: ')
second_number = input('Second number: ')

if second_number.isnumeric() == False:
    print('Please input a number. Closing the calculator!')
    exit ()

#if first_number.isnumeric() == False or second_number.isnumeric() == False:
    #print('Please input a number. Closing the calculator!')
    #exit()

first_number = int(first_number)
second_number = int (second_number)

result = 0
if operator == '+':
    #addition = first_number + second_number
    result = first_number + second_number
    label = 'addition'
    #print('Sum of {} and {} = '.format(first_number, second_number) + str(addition))
elif operator == '-':
    #substraction = first_number - second_number
    result = first_number - second_number
    label = 'substraction'
    #print('Substraction of {} and {} = '.format(first_number, second_number) + str(substraction))
elif operator == '*':
    #product = first_number * second_number
    result = first_number * second_number
    label = 'product'
    #print('Product of {} and {} = '.format(first_number, second_number) + str(product))
elif operator == '/':
    #division = first_number / second_number
    result = first_number / second_number
    label = 'division'
    #print('Division of {} and {} = '.format(first_number, second_number) + str(division))
elif operator == '%':
    #modulus = first_number % second_number
    result = first_number % second_number
    label = 'modulus'
    #print('Modulus of {} and {} = '.format(first_number, second_number) + str(modulus))
elif operator == '**':
    #exponent = first_number ** second_number
    result = first_number ** second_number
    label = 'exponent'
    #print('Exponent of {} and {} = '.format(first_number, second_number) + str(exponent))
else:
    print('Operation not recognized. Closing the calculator!')
    exit()

print(label + ' of ' + str(first_number) + ' ' + operator + ' ' + str(second_number) + ' equals ' + str(result))

