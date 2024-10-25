age = int(input("How old are you? "))
membership = str(input("Are you a member? (yes or no) "))
min_age = 18
if membership == "yes" and age >= min_age:
    print("You can register for the event.")
elif membership == "no":
    print("Sorry, you need to be a member to register for the event.")
else:
    print("Sorry, you need to be at least", min_age, "years old to register for the event.")