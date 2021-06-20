#program that performs mathematical operations on numbers.

""" first_value = int(input('Enter a number: '))
second_value = int(input('Enter another number: '))

sum = first_value + second_value
difference = first_value - second_value
product = first_value * second_value
quotient = first_value / second_value
modulus = first_value %  second_value
exponent = first_value ** second_value

print('Sum: ' + str(sum))
print('Difference: ' + str(difference))
print('Product: ' + str(product))
print('Quotient: ' + str(quotient))
print('Modulus: ' + str(modulus))
print('Exponent: ' + str(exponent))
 """

#PEMDAS (Parenthesis, Exponent, Multiplication, Division, Addition, Substraction) operation 
#print(3 + 4 * 5)
#print((3 + 4) * 5)

#code to convert a float into an int
#and to use the round() function  to perform rounding and conversion from a float value into an int value.

pi = 3.14
print(type(pi))
print(int(pi))
print('Round: ' + str(round(pi)))

uptime = 99.99
print(type(uptime))
print(int(uptime))
print('Round: ' + str(round(uptime)))

print(round(7.654321, 2)) #round to 2 decimal place
print(round(9.87654, 3)) #round to 3 decimal place