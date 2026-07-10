print("welcome to my expence tracker project ")
name = input("Entre your name : ")
food_expense = float(input("Enter food expense: "))
transport_expense = float(input("Enter transport expense: "))
shopping_expense = float(input("Enter shopping expense: "))
# Pehle total calculate karein (Inverted commas ke BAGAIR)
total_expense = food_expense + transport_expense + shopping_expense

# Ab is total ko print karein
print("Your total expense is:", total_expense)
