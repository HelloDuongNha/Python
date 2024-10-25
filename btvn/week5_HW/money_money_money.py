for day in range(1, 8):
    total_price = 0
    print(f'Day {day}:')
    more_groceries = True

    while more_groceries:
        name = input("Enter the grocery name: ")
        price = float(input("Enter the grocery price: "))
        total_price += price
        answer = input("wanna continue other groceries? (y/n): ")

        if answer.lower() != "y":
            more_groceries = False

    print(f"In day: {day} u spent{total_price}")
