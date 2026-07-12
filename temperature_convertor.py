convertor = [
  lambda c: c * 9 / 5 + 32,      # Celsius to Fahrenheit
  lambda f: (f - 32) * 5 / 9     # Fahrenheit to Celsius
]
name = input("what your name ?: ")
print("nice ",name)
choice = input(" enter C for celsius and F for fahrenheit: ").lower()
value = float(input("Enter the temperature: "))
if choice == "C":
    result = convertor[0](value)
    print(f"{value}°C = {result:.2f}°F")
elif choice == "F":
    result = convertor[1](value)
    print(f"{value}°F = {result :.2f}°C")    #   .2f ka matlab answer ko 2 decimal places tak dikhata hai.
else:
  print("Invalid choice! Please enter C or F.")
