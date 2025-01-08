

array1= [1,22,31,41]
array2= [1,22,31,41]

if len(array1) != len(array2):
  print('no son iguals')

iguals =True
for i in range(len(array1)):
  if array1[i] != array2[i]:
    iguals=False


if iguals:
  print("son iguals")
else: 
  print("no son iguals")

print("son iguals" if iguals else "no son iguals")



