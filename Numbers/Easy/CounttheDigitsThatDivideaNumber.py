# Count the Digits That Divide a Number
# https://leetcode.com/problems/count-the-digits-that-divide-a-number/description/
# Leetcode: 2520
# Difficulty: Easy

'''
Given an integer num, return the number of digits in num that divide num.

An integer val divides nums if nums % val == 0.

 

Example 1:

Input: num = 7
Output: 1
Explanation: 7 divides itself, hence the answer is 1.
Example 2:

Input: num = 121
Output: 2
Explanation: 121 is divisible by 1, but not 2. Since 1 occurs twice as a digit, we return 2.
Example 3:

Input: num = 1248
Output: 4
Explanation: 1248 is divisible by all of its digits, hence the answer is 4.
 

Constraints:

1 <= num <= 109
num does not contain 0 as one of its digits.
'''

class Solution:
  def countDigits(self, num: int) -> int:
    original = num
    digits = []

    while num > 0:
      digit = num % 10
      digits.append(digit)
      num = num // 10

    count = 0
    for d in digits:
      if d != 0 and original % d == 0:
        count += 1

    return count
  

if __name__ == '__main__':
  sol = Solution()
  print(sol.countDigits(num = 7)) # 1
  print(sol.countDigits(num = 121)) # 2
  print(sol.countDigits(num = 1248)) # 4
