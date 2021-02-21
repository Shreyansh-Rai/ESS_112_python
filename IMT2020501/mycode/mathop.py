def increment(n):
  return n + 1

def decrement(n):
  return n - 1

def add(x, y):
  mysum = x
  for i in range(y):
    mysum = increment(mysum)
  return mysum

def subtract(x, y):
  diff = x
  for i in range(y):
    diff = decrement(diff)
  return diff

def multiply(x, y):
  product = 0
  for i in range(y):
    product = add(product, x)
  return product

def divide(x, y):
  remainder = x
  quotient = 0
  while(remainder > 0):
    remainder = subtract(remainder, y)
  if(remainder == 0):
    return quotient
  else:
    return quotient + 1

def exponent(x, y):
  power = 1
  for i in range(y):
    power = multiply(power, x)
  return power
