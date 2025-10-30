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

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''

from typing import List
from collections import Counter

# Optimal solution
# Time Complexity: O(n)
# Space Complexity: O(n)

def isValidParanthesis(s: str) -> bool:
  stack = []
  paranthesis_map = {')': '(', '}': '{', ']': '['}

  for char in s:
    if char in paranthesis_map:
      top_element = stack.pop() if stack else '#'
      if paranthesis_map[char] != top_element:
        return False
    else:
      stack.append(char)
  
  return not stack

if __name__ == "__main__":
  s1 = "()[]{}"
  s2 = "(]"

  print("Optimal solution")
  result1 = isValidParanthesis(s1)
  result2 = isValidParanthesis(s2)
  if result1:
    print(f"{s1} is valid parentheses input")
  else:
    print(f"{s1} is not valid parentheses input")

  if result2:
    print(f"{s1} is valid parentheses input")
  else:
    print(f"{s1} is not valid parentheses input")