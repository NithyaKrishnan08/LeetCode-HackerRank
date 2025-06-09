# Prefix to Postfix Conversion

# TC: O(N)
# SC: O(N)
def PrefixToPostfix(s):
  n = len(s)
  st = []

  for i in range(n-1, -1, -1):
    ch = s[i]
    if ch.isalnum():
      st += ch
    else:
      top1 = st.pop()
      top2 = st.pop()
      new_converted = top1 + top2 + ch
      st.append(new_converted)

  return st[-1]

s = "*+pq-mn"
result = PrefixToPostfix(s)
print("Prefix Expression: ", s)
print("Postfix Expression: ", result)

