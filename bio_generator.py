# Day 2 Project: Profile & Story Generator
print("--- Welcome to the Profile Generator ---")

# 1. Strings (Text Data)
name = input("Enter your name: ")
role = input("What tech role are you learning? (e.g., Python Developer): ")

# 2. Integers (Whole Numbers)
age = int(input("Enter your age: "))
coding_days = int(input("How many days have you been coding?: "))

# 3. Booleans (True/False Logic)
is_loving_python = input("Are you enjoying Python? (yes/no): ").lower() == "yes"

# Calculating a future milestone using integer math
days_left = 100 - coding_days

# Outputting the results dynamically using variables
print("\n--- Generated Tech Profile ---")
print(f"Name: {name}")
print(f"Age: {age} years old")
print(f"Current Focus: Learning to become a {role}")
print(f"Status: Day {coding_days} of #100DaysOfCode ({days_left} days left to hit 100!)")
print(f"Is loving Python? {'Yes, absolutely! 🚀' if is_loving_python else 'It is challenging but fun! 💻'}")
