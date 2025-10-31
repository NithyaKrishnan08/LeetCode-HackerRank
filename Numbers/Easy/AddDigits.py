# Add Digits
# https://leetcode.com/problems/add-digits/description/
# Leetcode: 258
# Difficulty: Easy

'''
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

Example 1:
Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.

Example 2:
Input: num = 0
Output: 0
 

Constraints:
0 <= num <= 231 - 1
'''
class Solution:
  def addDigits(self, num: int) -> int:
    while num >= 10:
      total = 0
      while num > 0:
        digit = num % 10
        total += digit
        num = num // 10
      num = total
    return num
  
if __name__ == '__main__':
  sol = Solution()
  print(sol.addDigits(num = 38)) # 2
  print(sol.addDigits(num = 0)) # 0