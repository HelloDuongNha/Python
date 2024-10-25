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
for counter in range(n_randoms):
    randoms.append(randint(minimum, maximum))
randoms.sort()
print_list(randoms)

print(f"min = {min(randoms)}")
print(f"max = {max(randoms)}")
print(f"sum = {sum(randoms)}")
print(f"avg = {sum(randoms)/len(randoms)}")

print()
input("Press return to continue ...")
