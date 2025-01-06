
import math

# friends =5

# friends =friends + 1
# friends  += 1

# friends =friends - 1
# friends -= 1

# friends =friends * 3
# friends *=3

# friends =friends / 3
# friends /=3

# friends =friends ** 2
# friends **=2

# friends =friends % 2
# friends %=2

# print(friends)


# built-in functions
# x = 3.14
# y = 3
# z = 2

# result = abs(-x)
# result = round(x,0)
# result = pow(y,z)
# result = max(y,z)

# print(result)

# print(10**5)
# print(pow(10,5))

print(math.gcd(10,5))

# print(math.pi)

def custom_round(num:float, decimalAmount:int=0)->float:
    return round(num,decimalAmount)

print(custom_round(3.14159))