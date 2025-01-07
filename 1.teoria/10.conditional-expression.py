
# conditional expression



num = 5

print("Positive" if num > 0 else "Negative") # Positive

isPositive = True

label = "Positive" if isPositive else "Negative"


def isEven(num:int) -> str:
    if not isinstance(num, int):
        raise TypeError(f"Expected an int, got {type(num).__name__}")
    return "Even" if num % 2 == 0 else "Odd"


isEven(True)