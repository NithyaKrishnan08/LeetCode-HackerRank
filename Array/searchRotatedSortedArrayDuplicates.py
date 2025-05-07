'''
Problem Statement: Given an integer array arr of size N, sorted in ascending order (may contain duplicate values) and a target value k. Now the array is rotated at some pivot point unknown to you. Return True if k is present and otherwise, return False. 

Examples:

Example 1:
Input Format: arr = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6], k = 3
Result: True
Explanation: The element 3 is present in the array. So, the answer is True.

Example 2:
Input Format: arr = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6], k = 10
Result: False
Explanation: The element 10 is not present in the array. So, the answer is False. 
'''

# Brute force Solution - Linear Search
# Time Complexity - O(N)
# Time Complexity - O(1)

def searchTarget1(nums, target):
  n = len(nums)

  for i in range(1,n):
    if nums[i] == target:
      return True

  return False

# Optimal Solution - Binary Search
# Time Complexity - O(log N)
# Time Complexity - O(1)

def searchTarget2(nums, target):
  n = len(nums)
  low = 0
  high = n-1

  while (low <= high):
    mid = (low + high) // 2
    if(nums[mid] == target):
      return True
    
    if(nums[low] == nums[mid] and nums[mid] == nums[high]):
      low += 1
      high -= 1
      continue
    
    # left-sorted array
    if (nums[low] <= nums[mid]):
      if(nums[low] <= target and target <= nums[mid]):
        high = mid - 1
      else:
        low = mid + 1
    # right-sorted array
    else:
      if(nums[mid] <= target and target <= nums[high]):
        low = mid + 1
      else:
        high = mid - 1

  return False

if __name__ == "__main__":
  arr1 = [4,5,6,7,0,1,2,3]
  k1 = 0
  arr2 = [4,5,6,7,0,1,2]
  k2 = 3

  arr3 = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6]
  k3 = 3
  arr4 = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6]
  k4 = 10
  
  print("Brute force solution:")
  result1 = searchTarget1(arr1, k1)
  if not result1:
    print(f"Target {k1} is not present in {arr1}")
  else:
    print(f"Target {k1} is present in {arr1}")

  result2 = searchTarget1(arr2, k2)
  if not result2:
    print(f"Target {k2} is not present in {arr2}")
  else:
    print(f"Target {k2} is present in {arr2}")

  print("Optimal solution:")
  result3 = searchTarget2(arr3, k3)
  if not result3:
    print(f"Target {k3} is not present in {arr3}")
  else:
    print(f"Target {k3} is present in {arr3}")

  result4 = searchTarget2(arr4, k4)
  if not result4:
    print(f"Target {k4} is not present in {arr4}")
  else:
    print(f"Target {k4} is present in {arr4}")


