'''
Given a string with only characters X and Y. Find the minimum number of characters to remove from the string such that there is no interleaving of character X and Y and all the Xs appear before any Y.

Example 1:
Input:YXXXYXY

Output: 2
Explanation:
We can obtain XXXYY by:
Delete first Y -> XXXYXY
Delete last occurrence of X -> XXXYY
Example 2:

Input:YYXYXX
Output: 3
Explanation:
We can remove all occurrences of X or Y.

Example 3:
Input:XXYYYY
Output: 0
Explanation:
String matches the format required.
'''

def min_steps(s):
  num_y = 0
  min_del = 0
  for c in s:
    if c == 'X':
      min_del = min(num_y, min_del + 1)
    else:
      num_y += 1
  
  return min_del
