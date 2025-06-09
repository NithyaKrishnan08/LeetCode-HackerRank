'''
1. Reverse the given Infix Expression -> convert '(' to ')' and vice versa
2. Convert Infix to Postfix
3. Reverse the answer
'''

# Infix to Prefix Conversion

def reverseInfix(s):
  rev_s = list(s[::-1])
  for i in range(len(rev_s)):
    if rev_s[i] == '(':
      rev_s[i] = ')'
    elif rev_s[i] == ')':
      rev_s[i] = '('

  return ''.join(rev_s)


def priortity(ch):
  if ch == '^':
    return 3
  elif ch == '*' or ch == '/':
    return 2
  elif ch == '+' or ch == '-':
    return 1
  else:
    return -1

# TC: O(N)
# SC: O(N)
def InfixToPrefix(s):
  n = len(s)
  rev_s = reverseInfix(s)
  st = []
  ans = ""

  for ch in rev_s:
    if ch.isalnum():
      ans += ch
    elif ch == '(':
      st.append(ch)
    elif ch == ')':
      # pop all until open bracket
      while st and st[-1] != '(':
        ans += st.pop()
      # pop '('
      st.pop()
    else:
      while st and (ch != '^' and priortity(ch) <= priortity(st[-1])) or (ch == '^' and priortity(ch) < priortity(st[-1])):
        ans += st.pop()
      st.append(ch)

  while st:
    ans += st.pop()

  ans = ans[::-1]

  return ans

s = "(p+q)*(m-n)"
result = InfixToPrefix(s)
print("Infix Expression: ", s)
print("Prefix Expression: ", result)

