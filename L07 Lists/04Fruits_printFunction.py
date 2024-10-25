def print_list(items, header=None):
    if header != None:
        print(header)
    for item in items:
        print(f"{item}")
    print()


fruits = ["Banana","Orange","Apple","Mango"]

print_list(fruits)

print_list(fruits, "FRUITS")

print()
input("Press return to continue ...")
