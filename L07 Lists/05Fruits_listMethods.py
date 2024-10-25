def print_list(items, header=None):
    if header != None:
        print(header)
    for item in items:
        print(f"{item}")
    print()


fruits = ["Banana","Orange","Apple","Mango"]

print_list(fruits, "FRUITS")

fruits.sort()

print_list(fruits, "FRUITS sorted")

fruits.reverse()

print_list(fruits, "FRUITS reversed")

fruits.clear()

print_list(fruits, "No FRUITS :(")

print()
input("Press return to continue ...")
