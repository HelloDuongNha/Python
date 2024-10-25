from random import randint


def print_list(items, header=None):
    if header != None:
        print(header)
    for item in items:
        print(f"{item}")
    print()


# temporarily fix the list parameters
minimum = 1
maximum = 50
n_randoms = 7

randoms = set()
while len(randoms) < n_randoms:
    r = randint(minimum, maximum)
    randoms.add(r)

print_list(randoms, "Unordered set")

sorted_randoms = list(randoms)
sorted_randoms.sort()
print_list(sorted_randoms, "Sorted list")

print()
input("Press return to continue ...")
