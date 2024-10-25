from random import randint


def print_list(items, header=None):
    if header != None:
        print(header)
    for item in items:
        print(f"{item}")
    print()


minimum = int(input("Min: "))
maximum = int(input("Max: "))
n_randoms = int(input("How many random numbers? "))

randoms = []
for counter in range(n_randoms):
    randoms.append(randint(minimum, maximum))

randoms.sort()

print_list(randoms)

print()
input("Press return to continue ...")
