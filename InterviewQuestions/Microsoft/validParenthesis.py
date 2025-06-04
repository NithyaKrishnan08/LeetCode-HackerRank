'''
A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

S is empty;
S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

def solution(S)

that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..200,000];
string S is made only of the following characters: '(', '{', '[', ']', '}' and/or ')'.
'''

def solution(S):
  parenthesis_bracket = {
      '}': '{',
      ')': '(',
      ']': '['
  }

  stack = []
  for ch in S:
    if ch in "{[(":
      stack.append(ch)
    elif ch in ")]}":
      if not stack or stack[-1] != parenthesis_bracket[ch]:
        return 0
      stack.pop()

  return 1 if not stack else 0
  
if __name__ == "__main__":
  S = "{[()()]}"
  result = solution(S)
  print(result)