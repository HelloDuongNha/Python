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

randoms = []
while len(randoms) < n_randoms:
    r = randint(minimum, maximum)
    if r not in randoms:
        randoms.append(r)

randoms.sort()

print_list(randoms)

print()
input("Press return to continue ...")
