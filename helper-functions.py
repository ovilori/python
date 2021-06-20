#string helper functions
#three different ways to use the capitalize() function
#this program ensures the first character in the string is in uppercase
""" message = str.capitalize("first message") #calling it as a member of the str class
print(message)

message = "second message".capitalize() #calling it as a member of a literal string
print (message)

message = "third message"
print(message.capitalize()) """

#code to call functions that modify the case of the string

""" message = "hello world"
print(message.lower())
print(message.upper())

message = message.title()
print(message)
print(message.swapcase()) """

#this code returns the number of times a particular character is used in a string

""" location = "Mississippi"
print(location.count("s"))

#count how many characters are in a string

print(len("How many characters are in this string")) """

#this program calls functions that inspect the contents of a string

""" message = "carrace"

print(message.startswith("r"))
print(message.startswith("ca"))
print(message.startswith("ea"))

print(message.endswith("e"))
print(message.endswith("ce"))
print(message.endswith("ec")) """

#code to find the position of a position of a string inside another string
#the find() method locates the zero-based position of one string inside another string

""" message = "The quick brown fox jumps over the lazy dog"
print(message.find("q"))
print(message.find("t"))
print(message.find("T")) """

#code that strips empty characters from the left using lstrip or right using rstrip, or both using strip
""" message = "     theweekend       "

print("." + message.lstrip() + ".")
print("." + message.rstrip() + ".")
print(("." + message.strip() + ".")) """

#code that replaces one string found in another string

""" message = "Lagos is a beautiful place most of the times"
print(message.replace("beautiful", "shitty")) """

#code that justifies a string by adding empty space characters
message = "strange"

print(message.rjust(20))
print(message.rjust(20, "_"))
print(message.ljust(20))
print(message.ljust(20, "_"))
