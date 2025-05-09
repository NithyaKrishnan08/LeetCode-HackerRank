#  To check if the ith bit is set or not
#  Using left shift operator

def checkIthBitSet1(n, i):
  if (n & (1 << i) != 0):
    return True
  else:
    return False

result1 = checkIthBitSet1(13, 2)
if(result1):
  print("The ith bit is set")
else:
  print("The ith bit is not set")

#  Using right shift operator

def checkIthBitSet2(n, i):
  if ((n >> i) & 1 != 0):
    return True
  else:
    return False

result2 = checkIthBitSet2(13, 1)
if(result2):
  print("The ith bit is set")
else:
  print("The ith bit is not set")