'''
Problem Statement: Given an integer array arr of size N, sorted in ascending order (with distinct values) and a target value k. Now the array is rotated at some pivot point unknown to you. Find the index at which k is present and if k is not present return -1.

Example 1:

Example 1:
Input Format: arr = [4,5,6,7,0,1,2,3], k = 0
Result: 4
Explanation: Here, the target is 0. We can see that 0 is present in the given rotated sorted array, nums. Thus, we get output as 4, which is the index at which 0 is present in the array.

Example 2:
Input Format: arr = [4,5,6,7,0,1,2], k = 3
Result: -1
Explanation: Here, the target is 3. Since 3 is not present in the given rotated sorted array. Thus, we get the output as -1. 
'''

# Brute force Solution - Linear Search
# Time Complexity - O(N)
# Time Complexity - O(1)

def searchTarget1(nums, target):
  n = len(nums)

  for i in range(1,n):
    if nums[i] == target:
      return i

  return -1

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
      return mid
    
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

  return -1


if __name__ == "__main__":
  arr1 = [4,5,6,7,0,1,2,3]
  k1 = 0
  arr2 = [4,5,6,7,0,1,2]
  k2 = 3
  
  print("Brute force solution:")
  result1 = searchTarget1(arr1, k1)
  print(f"The index of target - {k1}: {result1}")

  result2 = searchTarget1(arr2, k2)
  print(f"The index of target - {k2}: {result2}")

  print("Optimal solution:")
  result3 = searchTarget2(arr1, k1)
  print(f"The index of target - {k1}: {result3}")

  result4 = searchTarget2(arr2, k2)
  print(f"The index of target - {k2}: {result4}")
