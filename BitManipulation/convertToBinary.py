'''
Bit Manipulation
'''

# Convert Decimal to Binary
# Time Complexity: O(log n)
# Space Complexity: O(log n)
def convertToBinary(n):
  result = ''
  while ( n != 0):
    if n % 2 == 1:
      result = '1' + result
    else:
      result = '0' + result
    n = n // 2
  return result

# Convert Decimal to Binary
# Time Complexity: O(length of string)
# Space Complexity: O(1)
def convertToDecimal(binaryString):
  n = len(binaryString)
  decimal = 0
  power2 = 1
  for i in range(n-1, -1, -1):
    if binaryString[i] == '1':
      decimal += power2
    power2 = power2 * 2

  return decimal

num1 = 13
result1 = convertToBinary(num1)
print(f"Binary number of {num1}: ", result1)

num2 = '1101'
result2 = convertToDecimal(num2)
print(f"Decimal number of {num2}: ", result2)