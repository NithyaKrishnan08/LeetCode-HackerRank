'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''
# Brute force Solution - Using division
import math

def productExceptSelf1(nums):
  if nums.count(0) > 1:
    return [0] * len(nums)

  if nums.count(0) == 1:
    zero_index = nums.index(0)
    result = [0] * len(nums)
    product_without_zero = 1
    for i, num in enumerate(nums):
      if i != zero_index:
        product_without_zero *= num
    result[zero_index] = product_without_zero
    return result

  totalProduct = math.prod(nums)
  result_nums = [totalProduct // num for num in nums]
  return result_nums

#  Optimized solution
#  Time Complexity: O(n)
#  Space Complexity: O(1)

def productExceptSelf2(nums):
  n = len(nums)
  result = [1] * n
  
  left_product = 1
  for i in range(n):
    result[i] = left_product
    left_product *= nums[i]

  right_product = 1
  for i in range(n-1, -1, -1):
    result[i] *= right_product
    right_product *= nums[i]

  return result  

if __name__ == "__main__":
  arr = [1,2,3,4]
  result1 = productExceptSelf1(arr)
  print("Output: ", result1)

  result2 = productExceptSelf2(arr)
  print("Output: ", result2)
