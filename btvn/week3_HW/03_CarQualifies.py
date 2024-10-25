speed = float(input("What is your car speed in km/h? "))
weight = float(input("What is your car weight in kg? "))
safety = int(input("What is your car safety rating from 1 to 10? "))
min_speed = 100
max_weight = 1800
min_safety = 7
if speed > min_speed and weight < max_weight and safety > min_safety:
    print("Your car qualifies for the racing event!")
else:
    print("Sorry, your car does not qualify for the racing event.")