'''
Problem Statement: Given an array of positive numbers ranging from 1 to n, such that all numbers from 1 to n are present except one number x, find x. Assume the input array is unsorted.
'''

def missing_number(arr):
  arr.sort()
  missing_no = 1
  for num in arr:
    if num == missing_no:
      missing_no += 1
    elif num > missing_no:
      break

  return missing_no