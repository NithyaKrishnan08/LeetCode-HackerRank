# Postfix to Infix Conversion

# TC: O(N) + O(N)
# SC: O(N)
def PostfixToInfix(s):
  st = []

  for ch in s:
    if ch.isalnum():
      st += ch
    else:
      top1 = st.pop()
      top2 = st.pop()
      new_converted = '(' + top2 + ch + top1 + ')'
      st.append(new_converted)

  return st[-1]

s = "pq+mn-*"
result = PostfixToInfix(s)
print("Postfix Expression: ", s)
print("Infix Expression: ", result)

