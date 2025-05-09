'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation:
n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:
Input: nums = [0,1]
Output: 2
Explanation:
n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation:
n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

Constraints:
n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique.
'''
#  Brute force solution
def missingNumber1(nums: list[int]) -> int:
  n = len(nums)
  expected_sum = n * (n + 1) // 2
  sum_of_n = 0
  for i in range(n):
    sum_of_n += nums[i]
  
  return expected_sum - sum_of_n

# Better solution
def missingNumber2(nums: list[int]) -> int:
  n = len(nums)
  number_set = set(range(n + 1))
  
  for num in nums:
    number_set.remove(num)

  return number_set.pop()

n1 = [3,0,1]
n2 = [0,1]
n3 = [9,6,4,2,3,5,7,0,1]
result1 = missingNumber1(n1)
result2 = missingNumber1(n2)
result3 = missingNumber1(n3)
print("Brute force solution")
print(f"The missing number in {n1}: {result1}")
print(f"The missing number in {n2}: {result2}")
print(f"The missing number in {n3}: {result3}")

result4 = missingNumber2(n1)
result5 = missingNumber2(n2)
result6 = missingNumber2(n3)
print("Better solution")
print(f"The missing number in {n1}: {result4}")
print(f"The missing number in {n2}: {result5}")
print(f"The missing number in {n3}: {result6}")