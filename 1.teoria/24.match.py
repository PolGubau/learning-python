
def day_of_week(day:int)->str:
  match day:
    case 1:
      return "Monday"
    case 2:
      return "Tuesday"
    case 3:
      return "Wednesday"
    case 4:
      return "Thursday"
    case 5:
      return "Friday"
    case 6:
      return "Saturday"
    case 7:
      return "Sunday"
    case _:
      return "Invalid day"
    
print(day_of_week(1)) # Monday


def isWeekend(day:str)->bool:
  match day:
    case "Saturday" | "Sunday":
      return True
    case _:
      return False
    
print(isWeekend("Saturday")) # True
print(isWeekend("Monday")) # False