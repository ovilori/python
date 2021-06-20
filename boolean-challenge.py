#this program prints one of several messages to the user based on their input.
#the user is prompted about whether they want to continue.
#if the user responds with either no or n, the phrase 'Exiting' is printed.

print("welcome!")
user_input = input("Would you like to continue? ")

if user_input == "no" or user_input == "n":
    print("exiting...")

# #if the user responds with either yes or y, print the phrases continuing ... and complete!

if user_input == "yes" or user_input == "y":
    print("continuing...")
    print (" ")
    print ("complete!")

# #if the user responds with anything else, print the phrase please try again and respond with yes or no.

else:
    print("Please try again and respond with yes or no")
