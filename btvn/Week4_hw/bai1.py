ask_again = True
while ask_again == True:
    try:
        exchange_rate = 23000
        usd = float(input("Enter an amount in USD: "))
        vnd = usd * exchange_rate
        print(f"{usd:.2f} USD is approximately {vnd:.3f} VND.")
        another_conversion = str(input("Do you want to convert another amount? (y/n): ").lower())
    except ValueError:
        print("Invalid input. Please try again.")
    if another_conversion == 'y' or another_conversion == 'yes':
        ask_again = True
    else:
        ask_again = False
print('BYEEEEEEEEEEEEE')

