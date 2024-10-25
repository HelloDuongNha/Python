def output(parameter1, parameter2):
    print(f"{parameter1} {parameter2}")


number1_str = input(" First number: ")
number1 = int(number1_str)

number2_str = input("Second number: ")
number2 = int(number2_str)

operation = input("Operation [+, -]: ")

if operation == "+":
    combination = number1 + number2
elif operation == "-":
    combination = number1 - number2

output("Answer:", combination)
output(combination, "is the answer")
output("Is this version better?", "Yes, I think so")
output("This version is better:", True)

print()
input("Press return to continue ...")
