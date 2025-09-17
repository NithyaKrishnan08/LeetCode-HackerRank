# Reverse Integer
# https://leetcode.com/problems/reverse-integer/description/
# Leetcode: 7

'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Constraints:
-231 <= x <= 231 - 1
'''

class Solution:
  def reverse(self, x: int) -> int:
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    rev = 0
    sign = -1 if x < 0 else 1
    x = abs(x)

    while x != 0:
      digit = x % 10
      x //= 10

      # checking the overflow befoe actually adding the digit
      if (rev > INT_MAX // 10) or (rev == INT_MAX // 10 and digit > INT_MAX % 10):
        return 0
      
      rev = rev * 10 + digit
    
    return sign * rev
  
if __name__ == "__main__":
  solution = Solution()
  x = 123
  print(f"Input: {x}")
  print(f"Output: {solution.reverse(x)}")

  x = -123
  print(f"Input: {x}")
  print(f"Output: {solution.reverse(x)}")