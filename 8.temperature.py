

unit = input("Is the temperature in (C)elsius or (F)ahrenheit: ")
temperature = float(input("Enter the temperature: "))

unit = unit.lower()
if unit not in ['c', 'f']:
    print("Please enter a valid unit")
    exit()


converted = 0

def printing_converted(unit, converted):
    print(f"The temperature is {round(converted,1)}° {unit}")

def from_celsius_to_fahrenheit(temperature:int):
    return round((temperature * 9/5) + 32,1)

def from_fahrenheit_to_celsius(temperature:int):
    return round((temperature - 32) * 5/9 ,1)


if unit == 'c':
    converted = from_celsius_to_fahrenheit(temperature)
    printing_converted('F', converted)
elif unit == 'f':
    converted = from_fahrenheit_to_celsius(temperature)
    printing_converted('C', converted)
else:
    print("Please enter a valid unit")
    exit()
