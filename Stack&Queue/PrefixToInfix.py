# Prefix to Infix Conversion

# TC: O(N) + O(N)
# SC: O(N)
def PrefixToInfix(s):
  n = len(s)
  st = []

  for i in range(n-1, -1, -1):
    ch = s[i]
    if ch.isalnum():
      st += ch
    else:
      top1 = st.pop()
      top2 = st.pop()
      new_converted = '(' + top1 + ch + top2 + ')'
      st.append(new_converted)

  return st[-1]

s = "*+pq-mn"
result = PrefixToInfix(s)
print("Prefix Expression: ", s)
print("Infix Expression: ", result)

