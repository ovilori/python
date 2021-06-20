#the format() helper function merges values into a literal string template without the need for string concatenation
#it can also format those merged values for proper display, as in the case of numbers, dates, and times.

""" medicine = "Paracetamol"
dosage = 5
duration = 4.5

instructions = "{} - Take {}ML by mouth every {} hours".format(medicine, dosage, duration)
print(instructions + "\n")

instructions = "{2} - Take {1}ML by mouth every {0} hours".format(medicine, dosage, duration)
print(instructions + "\n")

instructions = "{medicine} - Take {dosage}ML by mouth every {duration} hours".format(medicine = "Vitamin C", dosage = 10, duration = 6)
print(instructions + "\n")
 """

#code to use formatted string literals, or "f-strings"

""" name = "World"
message = f'Hello, {name}'
print(message)

count = 10
value = 3.14
message = f"Count to {count}. Multiply by {value}."
message = "Count to {}. Multiply by {}.".format(count, value)
#format string takes care of the data type conversion.
#hence, no need to call str() around the values.
print (message) """

#code to evaluate simple expressions in the replacement field of an f-string

""" width = 5
height = 10
print (f"The perimeter is {(2 * width) + (2 * height)}, and the area is {(width * height)}.") """

#code to define format specifiers to control alignment and padding
#format specifier uses a colon symbol (:) after the variable name
#to specify how that value should be formatted.

value = "hi"

#align the text to the left of a string that is 25 characters wide.
#"hi" occupires two of the 25 total characters
print(f".{value:<25}.") 

#align the text to the right of a string that is 25 characters wide.
print(f".{value:>25}.")

#place the text in the middle of a string that is 25 total characters wide.
print(f".{value:^25}.")

#preface the text with a single dash (-) instead of an empty space to fill the rest of the string.
print(f".{value:-^25}.")