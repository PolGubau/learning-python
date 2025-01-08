import math
def add(*args: int):
  sum=0
  for arg in args:
    sum = sum +arg
  return sum


print(add(1,1,1))

def display_full_name(*args):
  for arg in args:
    print(arg, end=" ")

display_full_name("John", "Doe", "Smith")


