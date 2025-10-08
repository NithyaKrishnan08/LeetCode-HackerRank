# Two Sum : Check if a pair with given sum exists in Array
# https://leetcode.com/problems/two-sum/description/
# Difficulty: Easy

'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
'''

# Brute Force Solution 
# Time Complexity - O(N^2)
# Space Complexity - O(N)
def twoSum1(nums, target):
  for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
      if nums[i] + nums[j] == target:
        return [i, j]
  return []

# Better Solution - O(N) - Optimal for indexes
# Time Complexity - O(N)
# Space Complexity - O(N)
def twoSum2(nums, target):
  seen = {}
  for i, num in enumerate(nums):
    complement = target - num
    if complement in seen:
      return [seen[complement], i]
    seen[num] = i
  return []

# Optimized Solution - O(N)
# Time Complexity - O(N) + O(N log N)
# Space Complexity - O(1)
def twoSum3(nums, target):
  sorted_nums = sorted(nums)
  left = 0
  right = len(sorted_nums) - 1

  while left < right:
    current_sum = sorted_nums[left] + sorted_nums[right]
    if (current_sum == target):
      return "YES"
    elif (current_sum < target):
      left += 1
    else:
      right -= 1
  return "NO"

nums = [1, 2, 3, 4]
target = 3
result = twoSum1(nums, target)
print("Brute Force Solution: ", result)

nums = [1, 2, 3, 4]
target = 3
result = twoSum2(nums, target)
print("Better Solution: ", result)

nums = [1, 2, 3, 4]
target = 3
result = twoSum3(nums, target)
print("Optimized Solution: ", result)

