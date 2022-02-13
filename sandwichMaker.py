#this program asks the customer for their sandwich preferences, calculate the cost and provides the order summary to the customer.
import pyinputplus as pyip
import time
bread_price = {'Wheat':100, 'White':200, 'Sourdough':100}
protein_price = {'Chicken':100, 'Turkey':200, 'Ham':100, 'Tofu':400}
cheese_price = {'Cheddar':100, 'Swiss':200, 'Mozzarella':100}
otherOption_price = {'Mayo':100, 'Mustard':200, 'Lettuce':100, 'Tomato':250}
print('Welcome to the BnB\'s Sandwich place.')
while True:
    name = input('Please enter your name: ')
    welcome_prompt = pyip.inputYesNo(f'Hello {name}, do you want a sandwich (enter yes or no)?: ')
    if welcome_prompt == 'no':
        print(f'{name}, Thank you for your time.')
        break

    print(f'Welcome {name}. Please follow the prompt to choose your Sandwich preference.')

    #choose a bread type
    bread_type = pyip.inputMenu(prompt='Please choose a breadtype: \n', choices=['Wheat', 'White', 'Sourdough'], numbered=True)
    breadCost = bread_price[bread_type]

    #choose a protein type
    protein_type = pyip.inputMenu(prompt='Please choose a protein type: \n', choices=['Chicken', 'Turkey', 'Ham', 'Tofu'], numbered=True)
    proteinCost = protein_price[protein_type]

    #choose cheese option
    cheese_option = pyip.inputYesNo('Do you want cheese (enter yes or no?: ')
    if cheese_option == 'no':
        cheeseCost = 0
        cheese_type = 'None'
    else:
        #choose the cheese type
        cheese_type = pyip.inputMenu(prompt='Please choose a cheese type: \n', choices=['Cheddar', 'Swiss', 'Mozzarella'], numbered=True)
        cheeseCost = cheese_price[cheese_type]

    #choose other options
    mayo_option = pyip.inputYesNo('Do you want Mayo?: ')
    if mayo_option == 'no':
        mayoCost = 0
    else:
        mayoCost = otherOption_price['Mayo']
    mustard_option = pyip.inputYesNo('Do you want Mustard?: ')
    if mustard_option == 'no':
        mustardCost = 0
    else:
        mustardCost = otherOption_price['Mustard']
    lettuce_option = pyip.inputYesNo('Do you want Lettuce?: ')
    if lettuce_option == 'no':
        lettuceCost = 0
    else:
        lettuceCost = otherOption_price['Lettuce']
    tomato_option = pyip.inputYesNo('Do you want Tomato?: ')
    if tomato_option == 'no':
        tomatoCost = 0
    else:
        tomatoCost = otherOption_price['Tomato']

    #ask for number of Sandwich to be made
    noofSandwich = pyip.inputInt('Please  enter the quantity of Sandwich to be made: ', default=1)

    #calculate customer's bill
    total_bill = (breadCost + proteinCost + cheeseCost + mayoCost + mustardCost + lettuceCost + tomatoCost) * noofSandwich

    time.sleep(1)
    print('..............................\nOrder Summary')
    print('..............................')
    print(f'Customer Name: {name}\n')
    print(f'Bread type: {bread_type}\nProtein type: {protein_type}\nCheese: {cheese_option} (type: {cheese_type})\nWith Mayo: {mayo_option}\nWith Mustard: {mustard_option}\nWith Lettuce: {lettuce_option}\nWith Tomato: {tomato_option}')
    print(f'''Quantity: {noofSandwich}\nTotal Bill: ${total_bill}\nThanks for choosing BnB's Sandwich Place.''')
    print('..............................')
    


    