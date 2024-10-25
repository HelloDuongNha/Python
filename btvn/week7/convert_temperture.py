def convert_temperature(value, unit):
    if unit not in ('F', 'C'):
        print("Invalid unit. Please enter F or C.")
        return None
    elif unit == 'F':
        result = (value - 32) * (5/9)
        print(f"{value} degrees Fahrenheit is equal to {result:.2f} degrees Celsius.")
    else:
        result = value * (9/5) + 32
        print(f"{value} degrees Celsius is equal to {result:.2f} degrees Fahrenheit.")
    return result
value = float(input('what is your degree: '))
unit = input('in what unit? (F/C):').upper()
convert_temperature(value, unit)
