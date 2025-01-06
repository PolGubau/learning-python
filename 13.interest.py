#compound interest calc

principle =0
rate = 0
time = 0

while principle <= 0:
    try:
        principle = float(input("Enter the principle amount: "))
    except ValueError:
        print("Please enter a valid number")

    if(principle <= 0):
        print("Principle amount must be greater than 0")

while rate <= 0:
    try:
        rate = float(input("Enter the rate of interest: "))
    except ValueError:
        print("Please enter a valid number")

    if(rate <= 0):
        print("Rate of interest must be greater than 0")
  
while time <= 0:
    try:
        time = float(input("Enter the time in years: "))
    except ValueError:
        print("Please enter a valid number")

    if(time <= 0):
        print("Time must be greater than 0")
    
compound_interest = principle * (pow((1 + rate / 100), time))

print(f"The compound interest is: {compound_interest:.2f}")