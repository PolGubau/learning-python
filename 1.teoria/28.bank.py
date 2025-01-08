def showBalance():
  print("_______________________________")
  print(f"Your balance is: {balance:>10,.2f}€")  
  print("_______________________________")

def deposit()->float:
  amount = float(input("Enter amount to deposit: "))
  
  if(amount < 0):
    print("🟥 Invalid amount")
    return 0
  else:
    return amount
  

  

def withdraw()-> float:
  amount = float(input("Enter amount to deposit: "))
  if(amount < 0):
    print("🟥 Invalid amount")
    return 0
  
  if balance > amount:
    return amount
  else:
    print("🟥 Insufficient funds")
    return 0


balance:float = 0.00
running = True


while running:
  print("Hello, welcome to the bank!")

  print("1. Show balance")
  print("2. Deposit")
  print("3. Withdraw")
  print("4. Exit")

  choice = int(input("Enter your choice (1-4): "))
 
  match choice:
    case 1:
      showBalance()
    case 2:
      balance +=deposit()
      showBalance()
    case 3:
      balance -= withdraw()
      showBalance()
    case 4:
      running = False
      print("Thank you for using the bank!")
    case _:
      print("🟥 Invalid choice")
      continue

        
