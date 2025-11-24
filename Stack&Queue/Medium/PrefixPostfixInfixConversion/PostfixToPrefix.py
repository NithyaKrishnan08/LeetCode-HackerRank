# Postfix to Prefix Conversion

# TC: O(N)
# SC: O(N)
def PostfixToPrefix(s):
  st = []

  for ch in s:
    if ch.isalnum():
      st += ch
    else:
      top1 = st.pop()
      top2 = st.pop()
      new_converted = ch + top2 + top1
      st.append(new_converted)

  return st[-1]

s = "pq+mn-*"
result = PostfixToPrefix(s)
print("Postfix Expression: ", s)
print("Prefix Expression: ", result)

