customers = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve', 'Mike', 'John']
tickets = [15, 23, 7, 12, 6, 10, 20]

name = input("Enter the customer name: ")

# Print the number of tickets that he/she bought
if name in customers:
    index = customers.index(name)
    print(f"{name} bought {tickets[index]} tickets.")
else:
    print("Invalid customer name.")

#Find the customer that bought the most number of tickets
max_tickets = max(tickets)
max_index = tickets.index(max_tickets)
max_customer = customers[max_index]
print(f"The customer that bought the most number of tickets is {max_customer} with {max_tickets} tickets.")

#Find the customers that number of tickets they bought are greater than the average number of tickets
average_tickets = sum(tickets) / len(tickets)
above_average_customers = []
for i in range(len(customers)):
    if tickets[i] > average_tickets:
        above_average_customers.append(customers[i])
print(f"The customers that number of tickets they bought are greater than the average number of tickets are {', '.join(above_average_customers)}.")
