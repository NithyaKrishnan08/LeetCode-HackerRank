# Pow(x, n)
# https://leetcode.com/problems/powx-n/description/
# LeetCode Problem 50

'''
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 

Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
n is an integer.
Either x is not zero or n > 0.
-104 <= xn <= 104
'''

class Solution:
  # TC: O(log n)
  # SC: O(log n) for recursion stack space
  def myPow(self, x: float, n: int) -> float:
    def pow_helper(x, n):
      if n == 0:
        return 1.0
      
      if n < 0:
        return 1 / pow_helper(x, -n)
      
      if n % 2 == 0:
        half = pow_helper(x, n // 2)
        return half * half
      
      # If n is odd
      
      return x * pow_helper(x, n - 1)
    
    return pow_helper(x, n)
    
if __name__ == "__main__":
  sol = Solution()
  print(sol.myPow(2.00000, 10))  # Output: 1024.00000
  print(sol.myPow(2.10000, 3))   # Output: 9.26100
  print(sol.myPow(2.00000, -2))  # Output: 0.25000