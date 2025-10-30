# Maximum Nesting Depth of the Parentheses
# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/
# Leetcode: 1614
# Difficulty: Easy

'''
Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.

 

Example 1:

Input: s = "(1+(2*3)+((8)/4))+1"

Output: 3

Explanation:

Digit 8 is inside of 3 nested parentheses in the string.

Example 2:

Input: s = "(1)+((2))+(((3)))"

Output: 3

Explanation:

Digit 3 is inside of 3 nested parentheses in the string.

Example 3:

Input: s = "()(())((()()))"

Output: 3

 

Constraints:

1 <= s.length <= 100
s consists of digits 0-9 and characters '+', '-', '*', '/', '(', and ')'.
It is guaranteed that parentheses expression s is a VPS.
'''
class Solution:
  def maxDepth(self, s: str) -> int:
    depth, max_depth = 0, 0
    
    for ch in s:
      if ch == '(':
        depth += 1
        max_depth = max(max_depth, depth)
      elif ch ==')':
        depth -= 1

    return max_depth
  
if __name__ == '__main__':
  sol = Solution()
  print(sol.maxDepth(s = "(1+(2*3)+((8)/4))+1")) # 3
  print(sol.maxDepth(s = "(1)+((2))+(((3)))")) # 3
  print(sol.maxDepth(s = "()(())((()()))")) # 3
