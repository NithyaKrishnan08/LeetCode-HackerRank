'''
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
'''

# Brute force Solution
# Time Complexity - O(N)
# Time Complexity - O(1)

def findMin1(nums):
  minNum = nums[0]
  n = len(nums)

  for i in range(1,n):
    if nums[i] < minNum:
      minNum = nums[i]

  return minNum

# Optimal Solution
# Time Complexity - O(log N)
# Time Complexity - O(1)

def findMin2(nums):
  n = len(nums)
  low = 0
  high = n-1
  minNum = float('inf')

  while (low <= high):
    mid = (low + high) // 2
    
    # left-sorted array
    if (nums[low] <= nums[mid]):
      minNum = min(minNum, nums[low])
      low = mid + 1
    # right-sorted array
    else:
      minNum = min(minNum, nums[mid])
      high = mid - 1

  return minNum

if __name__ == "__main__":
  arr1 = [3,4,5,1,2]
  arr2 = [4,5,6,7,0,1,2]
  
  print("Brute force solution:")
  result1 = findMin1(arr1)
  print(f"The minimum in the rotated sorted array: {arr1} is {result1}")

  result2 = findMin1(arr2)
  print(f"The minimum in the rotated sorted array: {arr2} is {result2}")

  print("Optimal solution:")
  result3 = findMin2(arr1)
  print(f"The minimum in the rotated sorted array: {arr1} is {result3}")

  result4 = findMin2(arr2)
  print(f"The minimum in the rotated sorted array: {arr2} is {result4}")
