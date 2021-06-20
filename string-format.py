#code to compare literal strings defined by using single and double quotation marks

""" first_string = 'A literal string'
second_string = "A literal string"

print(first_string == second_string) """

#this code uses quotes inside other quotes

""" third_string = 'A single quoted literal string with a " double quote'
fourth_string = "A doubled quoted literal string with a ' single quote"

print(third_string)
print(fourth_string) """

#this code uses the \ character to create an escape sequence.

""" fifth_string = 'A single quoted literal string with an \' escaped single quote'
sixth_string = "A double quoted literal string with a \" double quote"
seventh_string = 'A literal string with a \n new line character'
eight_string = 'A literal string with a \t tab character'

print(fifth_string)
print(sixth_string)
print(seventh_string)
print(eight_string) """

#this code displays raw strings by adding a prefix "r"  
#to a literal string to produce a raw output, without any escaping

""" ninth_string = r"A literal string with a \n new line character printed raw"
print(ninth_string) """

#this code uses multi-line strings to display on multiple lines instead of using the new line escape sequence.

# tenth_string = '''A literal string
# on more than one line
# sometimes known as a verbatim string'''

# eleventh_string = """A literal string
#         on more than one line
# sometimes known as a verbatim string"""

# print(tenth_string + "\n")
# print(eleventh_string)

#this program formats strings by using the print () function

first = "Olamide"
second = "Vincent"
third = "Ilori"

print(first,second)
print(first, second, third)
print(first, second, third, sep="-")
print(first, second, third, sep="-", end=".")
