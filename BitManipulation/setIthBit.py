#  To set ith bit of a number
#  Using right shift operator

def setIthBit(n, i):
  return n | (i << i)

result1 = setIthBit(13, 1)
print("The ith bit is set: ", result1)