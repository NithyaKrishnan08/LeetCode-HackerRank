# Maximum subarray
# https://leetcode.com/problems/maximum-subarray/description/
# Difficulty: Medium
# Kadane's algorithm

'''
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
'''

# Brute force Solution
# Time Complexity - O(N^3)
# Time Complexity - O(1)
def maxSubArray1(nums):
  maximumSum = -float('inf')

  n = len(nums)
  for i in range(n):
    for j in range(i, n):
      subSum = 0
      for k in range(i, j+1):
        subSum += nums[k]

      maximumSum = max(maximumSum, subSum)

  return maximumSum

# Better Solution
# Time Complexity - O(N^2)
# Time Complexity - O(1)
def maxSubArray2(nums):
  maximumSum = -float('inf')

  n = len(nums)
  for i in range(n):
    subSum = 0
    for j in range(i, n):
      subSum += nums[j]
      maximumSum = max(maximumSum, subSum)

  return maximumSum

# Optimal Solution - Kadane's Algorithm
# Time Complexity - O(N)
# Time Complexity - O(1)

def maxSubArray3(nums):
  maximumSum = -float('inf')
  subSum = 0
  n = len(nums)
  for i in range(n):
    subSum += nums[i]

    if (subSum > maximumSum):
      maximumSum = subSum
    
    if (subSum < 0):
      subSum = 0

  return maximumSum

# Optimal Solution - Kadane's Algorithm - to display the sub-array
# Time Complexity - O(N)
# Time Complexity - O(1)

def maxSubArray4(nums):
  maximumSum = -float('inf')
  subSum = 0
  n = len(nums)
  startIndex = -1
  endIndex = -1
  subArray = []

  for i in range(n):
    if (subSum == 0):
      start = i

    subSum += nums[i]

    if (subSum > maximumSum):
      maximumSum = subSum
      startIndex = start
      endIndex = i
    
    if (subSum < 0):
      subSum = 0

  for i in range(startIndex, endIndex + 1):
    subArray.append(nums[i])

  return maximumSum, subArray

if __name__ == "__main__":
  arr = [-2,1,-3,4,-1,2,1,-5,4]
  
  result1 = maxSubArray1(arr)
  print("Brute force solution - The largest sum of the sub-array: ", result1)

  result2 = maxSubArray2(arr)
  print("Better solution - The largest sum of the sub-array", result2)

  result3 = maxSubArray3(arr)
  print("Optimal solution - The largest sum of the sub-array", result3)

  result4 = maxSubArray4(arr)
  print("Optimal solution - The largest sum of the sub-array", result4[0])
  print("Optimal solution - The largest sub-array", result4[1])