# Infix to Postfix Conversion
def priortity(ch):
  if ch == '^':
    return 3
  elif ch == '*' or ch == '/':
    return 2
  elif ch == '+' or ch == '-':
    return 1
  else:
    return -1

# TC: O(N) + O(N)
# SC: O(N) + O(N)
def InfixToPostfix(s):
  n = len(s)
  st = []
  ans = ""

  for i in range(n):
    if s[i].isalnum():
      ans += s[i]
    elif s[i] == '(':
      st.append(s[i])
    elif s[i] == ')':
      # pop all until open bracket
      while st and st[-1] != '(':
        ans += st.pop()
      # pop '('
      st.pop()
    else:
      while st and priortity(s[i]) <= priortity(st[-1]):
        ans += st.pop()
      st.append(s[i])

  while st:
    ans += st.pop()

  return ans

s = "(p+q)*(m-n)"
result = InfixToPostfix(s)
print("Infix Expression: ", s)
print("Postfix Expression: ", result)

