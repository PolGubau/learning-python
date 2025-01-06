weight = float(input("Enter your weight: "))
unit = input("Is your weight in (L)bs or (K)g: ")

if unit.lower() not in ['l', 'k']:
    print("Please enter a valid unit")
    exit()


converted = 0



def printing_converted(unit, converted):
    print(f"You are {round(converted,1)} {unit}")

if unit.lower() == 'l':
    converted = weight * 0.45
    printing_converted('Kg', converted)

if unit.lower() == 'k':
    converted = weight / 0.45
    printing_converted('Lbs', converted)





