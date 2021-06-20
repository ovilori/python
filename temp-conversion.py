#this program converst temperature from Fahrenheit to Celsius
#prompts users for a temperature in Fahrenheit
#performs the conversion to Celsius, and then displays the Celsius temperature.

Fahrenheit_value = input('What is the temperature in fahrenheit? ')

if Fahrenheit_value.isnumeric() == False:
    print('Input is not a number')
    exit()

Fahrenheit_value = int(Fahrenheit_value)
Celsius = (Fahrenheit_value - 32) * 5/9

print('Temperature in celsius is: ' + str(round(Celsius, 2)))
