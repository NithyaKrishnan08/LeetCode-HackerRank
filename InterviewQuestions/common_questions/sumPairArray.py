'''
Problem Statement: Given an array of integers and a value, determine if there are any two integers in the array whose sum is equal to the given value. Return true if the sum exists, and false if it does not. Consider the following array and its target sums:
'''

def sumPair(arr, target):
  arr.sort()
  low = 0
  high = len(arr) - 1

  while low <= high:
    if arr[low] + arr[high] == target:
      return True
    elif arr[low] + arr[high] < target:
      low = low + 1
    else:
      high = high - 1

  return False

if __name__ == "__main__":
  arr = [5, 7, 1, 2, 8, 4, 3]
  target = 19

  result = sumPair(arr, target)
  print(result)