#program to create a list of colors. Define a list by using a set of [] brackets
#print the list and type to the console

colors = ['brown', 'red', 'blue', 'purple', 'yellow', 'white', 'green'] 
#print(colors)
#print(type(colors))

#using an zero-based numeric value to access individual element of the list.

#print(f'0-based indexing into the list ...second item: {colors[1]}')
#print(f'Last item of the list: {colors[-1]}')
#print(f'The item before the last item: {colors[-2]}')

#creating a slice
#a slice defines a range of elements by using a special syntax. 
#it uses a colon (:) to seperate the beginning of the slice on the left, and end of the slice on the right.
#value on the left is inclusive, value on the right of the slice is exclusive

print(f'\nPrint a slice starting at index 2 and excluding index 5:')
print(colors[2:5])
print(type(colors))

print(f'\nPrint a slice starting from index 0 and ending at index 3:')
print(colors[:3])

print(f'\nPrint a slice starting at index 4 to the end of the list:')
print(colors[4:])

print('\nPrint a slice, from the 4th from the end, but without the last item:')
print(colors[-4:-1])

#reverse the list with the reverse helper function

colors.reverse
print('\nreversed: ', colors)

#sort the list alphabetically with the sort helper fucntion

colors.sort()
print('\nsorted: ', colors)

#treating the list like a queue
#a queue refers to a list that stores items in the order in which they were added.
#a pop operation removes an item from the queue for processing ('first in, first out i.e FIFO or 'last in, first out' i.e LIFO).

#color = colors.pop(0) #takes the first item in the list and assigns it to the variable color for processing
#print('\npopped color: ', color)

#add and remove items from the list using the helper functions append() & remove()
print('\nold_colors: ', colors)
colors.append('black')
colors.append('pink')
print('\ncolors_added: ', colors)

colors.remove('white')
colors.remove('blue')
print('\ncolors_removed: ', colors)

#combining a list with another list using the helper function extend()
new_colors = ['violet', 'orange', 'grey']
colors.extend(new_colors)
print('\nextended_colors: ', colors)

#clearing all items from a list using the clear() function

colors.clear()
print('\ncleared_colors: ', colors)

#add any data type to a list
#sundry = ['John', True, 3.14, 7]
#print(sundry)
#print(type(sundry))

#create an empty list
#my_list = []


