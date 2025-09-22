# Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/description/
# Leetcode: 20

'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''

class Solution:
  def isValid(self, s: str) -> bool:
    stack = []
    parenthesis_map = {')': '(', '}': '{', ']': '['}

    for char in s:
      if char in parenthesis_map:
        top_element = stack.pop() if stack else '#'
        if parenthesis_map[char] != top_element:
          return False
      else:
        stack.append(char)

    return not stack
  
if __name__ == "__main__":
  solution = Solution()
  s = "()"
  print(f"Input: {s}")
  print(f"Output: {solution.isValid(s)}")

  s = "()[]{}"
  print(f"Input: {s}")
  print(f"Output: {solution.isValid(s)}")

  s = "(]"
  print(f"Input: {s}")
  print(f"Output: {solution.isValid(s)}")

  s = "([])"
  print(f"Input: {s}")
  print(f"Output: {solution.isValid(s)}")

  s = "([)]"
  print(f"Input: {s}")
  print(f"Output: {solution.isValid(s)}")