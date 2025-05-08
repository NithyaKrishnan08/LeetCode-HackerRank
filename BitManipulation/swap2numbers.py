#  Swap two numbers without third variable without using arithmetic operations
#  Using XOR operator
def swapNumbers(a, b):
  print(f"Before swapping: a = {a}, b = {b}")
  a = a ^ b
  b = a ^ b
  a = a ^ b
  print(f"After swapping: a = {a}, b = {b}")

swapNumbers(5, 10)