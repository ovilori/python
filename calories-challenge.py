#This program is a calorie counter that will calculate the sum of calories taken daily.
#asks user for date
#aks for calories taken for breakfast, lunch, dinner and snacks.
#calculates the sum and display as a message.

#First, ask the user for today's date
print("What is Today's date")
date_today = input()
#Now, let us have the amount of calories taken today
print("Enter amount of Breakfast Calories eaten today")
breakfast_calories = int(input())
print("Enter the amount of Lunch calories eaten today")
lunch_calories = int(input())
print("Enter the amount of Dinner calories eaten today")
dinner_calories = int(input())
print("Enter the amount of Snack calories eaten today")
snack_calories = int(input())
#Next, sum the calories
calories_sum = (breakfast_calories + lunch_calories + dinner_calories + snack_calories)
#Print a message to display the amount of calories taken today
print("Calories content for " + date_today + ": " + str(calories_sum))