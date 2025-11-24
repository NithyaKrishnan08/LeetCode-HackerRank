# Next Greater Element III
# https://leetcode.com/problems/next-greater-element-iii/description/
# Leetcode: 556
# Difficulty: Medium

'''
Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.

Example 1:
Input: n = 12
Output: 21

Example 2:
Input: n = 21
Output: -1

Constraints:
1 <= n <= 231 - 1
'''
from typing import List

class Solution:
  # Optimal solution
  # TC: O(4N)
  # SC: O(2N)
  def nextGreaterNumber(self, n: int) -> int:
    digits = list(str(n))
    L = len(digits)

    # 1. Find the first decreasing digit from the right
    i = L - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
      i -= 1

    if i < 0:
      return -1 # digits are in descending order

    # 2. Find the next largest digit to swap with digits[i]
    j = L - 1
    while digits[j] <= digits[i]:
      j -= 1

    # 3. Swap digits[i] and digits[j]
    digits[i], digits[j] = digits[j], digits[i]

    # 4. Reverse the suffix starting at i + 1
    digits[i + 1:] = reversed(digits[i + 1:])

    # 5. Convert back to integer
    result = int(''.join(digits))

    # 6. Check if result fits in 32-bit integer
    return result if result < 2**31 else -1
  
if __name__ == "__main__":
  n = 12
  solution = Solution()
  result = solution.nextGreaterNumber(n)
  print(result)