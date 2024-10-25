purchase = float(input("How much did you spend? "))
location = str(input("Where are you located? "))
min_purchase = 100
eligible_location = "Ha Noi"
if purchase >= min_purchase and location == eligible_location:
    print("Congratulations, you are eligible for the promotion!")
else:
    print("Sorry, you are not eligible for the promotion.")