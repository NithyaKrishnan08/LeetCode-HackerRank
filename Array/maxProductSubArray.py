'''
Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''

# Brute force Solution
# Time Complexity - O(N^3)
# Time Complexity - O(1)

def maxProductSubArray1(nums):
  maxProduct = -float('inf')
  n = len(nums)

  for i in range(n):
    for j in range(i, n):
      subProduct = 1
      for k in range(i, j+1):
        subProduct *= nums[k]

      maxProduct = max(maxProduct, subProduct)

  return maxProduct

# Better Solution
# Time Complexity - O(N^2)
# Time Complexity - O(1)

def maxProductSubArray2(nums):
  maxProduct = -float('inf')
  n = len(nums)

  for i in range(n):
    subProduct = 1
    for j in range(i, n):
      subProduct *= nums[j]
      maxProduct = max(maxProduct, subProduct)

  return maxProduct

# Optimal Solution - Kadane's Algorithm
# Time Complexity - O(N)
# Time Complexity - O(1)



# Optimal Solution - Kadane's Algorithm - to display the sub-array
# Time Complexity - O(N)
# Time Complexity - O(1)


if __name__ == "__main__":
  arr1 = [2,3,-2,4]
  arr2 = [-2,0,-1]
  
  print("Brute force solution:")
  result1 = maxProductSubArray1(arr1)
  print(f"The largest product of subarray: {arr1} is {result1}")

  result2 = maxProductSubArray1(arr2)
  print(f"The largest product of subarray: {arr2} is {result2}")

  print("Better solution:")
  result3 = maxProductSubArray2(arr1)
  print(f"The largest product of subarray: {arr1} is {result3}")

  result4 = maxProductSubArray2(arr2)
  print(f"The largest product of subarray: {arr2} is {result4}")