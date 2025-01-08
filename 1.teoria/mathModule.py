pi = 3.141592653589793

def square(x):
  return x*x

def cube(x):
  return x*x*x

def circleArea(r):
  return pi * square(r)

def sphereVolume(r):
  return 4/3 * pi * cube(r)

def cylinderVolume(r,h):
  return pi * square(r) * h

def coneVolume(r,h):
  return 1/3 * pi * square(r) * h

def torusVolume(R,r):
  return 2 * pi * square(r) * pi * square(R)

def squarePerimeter(x):
  return 4 * x

def rectanglePerimeter(x,y):
  return 2 * (x + y)

def circlePerimeter(r):
  return 2 * pi * r

def trianglePerimeter(a,b,c):
  return a + b + c

def trapezoidPerimeter(a,b,c,d):
  return a + b + c + d

def parallelogramPerimeter(a,b):
  return 2 * (a + b)