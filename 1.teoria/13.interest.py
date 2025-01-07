#compound interest calc

principle =0
rate = 0
time = 0

def get_input(inputMessage:str, errorMessage:str):
    while True:
        try:
            userInput = float(input(inputMessage))
            if userInput <= 0:
                print(errorMessage)
            else:
                return userInput
        except ValueError:
            print("Please enter a valid number")



principle = get_input("Enter the principle amount: ", "Principle amount must be greater than 0")

rate = get_input("Enter the rate of interest: ", "Rate of interest must be greater than 0")

time = get_input("Enter the time in years: ", "Time must be greater than 0")
    
compound_interest = principle * (pow((1 + rate / 100), time))

print(f"The compound interest is: {compound_interest:.2f} €")