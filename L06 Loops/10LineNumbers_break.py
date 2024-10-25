n_lines = int(input("How many lines? "))
for counter in range(1, n_lines+1):
    if counter == 3:
        break
    print(f"This is line {counter}")

print()
input("Press return to continue ...")
