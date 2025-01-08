 

def drawBoard(files=5, cols=5,c1="⬛",c2="⬜"):
  for f in range(files):
    for c in range(cols):
      if f%2==0:  
        if c%2==0:   
          print(c1,end=" ")
        else:
          print (c2,end=" ")
      else:
        if c%2==0: 
          print (c2,end=" ")
        else:
          print(c1,end=" ")
    print("")


drawBoard()
 