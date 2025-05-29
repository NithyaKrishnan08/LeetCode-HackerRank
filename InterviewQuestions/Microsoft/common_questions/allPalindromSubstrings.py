'''
Problem Statement: Reverse the order of words in a given sentence.

Example: "sphinx of black quartz judge my vow" should output as "vow my judge quartz black of sphinx"
'''

def find_palindromic_substrings(s):
  palindromes = set()

  def expand(left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
      if right - left + 1 >= 2:
        palindromes.add(s[left:right+1])
      left -= 1
      right += 1

  for i in range(len(s)):
    expand(i, i)
    expand(i, i+1)

  return list(palindromes)

if __name__ == "__main__":
  input = "poppopo"

  result = find_palindromic_substrings(input)
  print(result)