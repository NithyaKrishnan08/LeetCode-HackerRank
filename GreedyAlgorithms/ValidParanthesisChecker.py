# Valid Paranthesis String

'''
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "(*)"
Output: true
Example 3:

Input: s = "(*))"
Output: true
 

Constraints:

1 <= s.length <= 100
s[i] is '(', ')' or '*'.
'''

class Solution:
  # Brute Force Solution - Recursive Method
  # TC: O(3^N)
  # SC: O(N)
  def checkValidString1(self, s: str) -> bool:
    n = len(s)

    def checkString(index, count):
      if count < 0:
        return False
    
      if index == n:
        return count == 0
        
      if s[index] == '(':
        return checkString(index + 1, count + 1)
      
      if s[index] == ')':
        return checkString(index + 1, count - 1)
      
      return checkString(index + 1, count + 1) or checkString(index + 1, count - 1) or checkString(index + 1, count)
    
    return checkString(0, 0)
  
  # Optimal Solution - Greedy Algorithn
  # TC: O(N)
  # SC: O(1)
  def checkValidString(self, s: str) -> bool:
    min_open = max_open = 0

    for char in s:
      if char == '(':
        min_open += 1
        max_open += 1
      elif char == ')':
        min_open -= 1
        max_open -= 1
      else:  # char == '*'
        min_open -= 1   # '*' as ')'
        max_open += 1   # '*' as '('

      # Make sure min_open doesn't go negative
      if min_open < 0:
        min_open = 0

      # Too many unmatched ')' — invalid
      if max_open < 0:
        return False

    return min_open == 0

  
if __name__ == "__main__":
  solution = Solution()
  s = "(((((()*)(*)*))())())(()())())))((**)))))(()())()"
  result = solution.checkValidString(s)
  print(result)
    
      
    