name = input("What is your name? ")
age = input("What is your age? ")
numerical_age = int(age)
year = 2020
year_of_birth = year - numerical_age
print("Hello " + age + " year old " + name)
print("You were born in " + str(year_of_birth))

print()
input("Press return to continue ...")
