# nested loops in python


rows = 5
cols = 5
symbol = "*"

for i in range(rows):
    for j in range(cols):
        print(symbol, end=" ")
    print()

# Output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


