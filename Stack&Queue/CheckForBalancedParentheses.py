# Check for Balanced Parenthesis

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

class Solution:
  def isValid(self, s: str) -> bool:
    stack = []
    paranthesis_map = {
      ')': '(',
      ']': '[',
      '}': '{'
    }
    for char in s:
      if char in paranthesis_map:
        top_element = stack.pop() if stack else '#'
        if paranthesis_map[char] != top_element:
          return False
      else:
        stack.append(char)

    return not stack
  
if __name__ == "__main__":
  solution = Solution()
  s = "(]"
  result = solution.isValid(s)
  print(result)