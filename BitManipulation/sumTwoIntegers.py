def getSum(a: int, b: int) -> int:
  mask = 0xffffffff
  max_int = 0x7fffffff

  while b != 0:
      carry = ((a & b) << 1) & mask
      a = (a ^ b) & mask # sum without carry
      b = carry
  
  if a > max_int:
      a = ~(a ^ mask)
  
  return a

result = getSum(1, 2)
print(f"Sum: {result}")