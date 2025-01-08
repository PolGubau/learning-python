# list comprehension

doubles = []

for x in range(1,11):
    doubles.append(x*2)


print(doubles)

# -----

doubles = [x*2 for x in range(1,11)]




fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']

upperFruits = [fruit.upper() for fruit in fruits]

print(upperFruits)

numbers =[1,-2,3,-4,5,-6,7,-8,9]

positiveNumbers = [number for number in numbers if number > 0]
negativeNumbers = [number for number in numbers if number < 0]
evenNums = [number for number in numbers if number % 2 == 0]
oddNums = [number for number in numbers if number % 2 != 0]
def greaterThan(x):
  return [number for number in numbers if number > x]
