'''
Problem Statement: Reverse the order of words in a given sentence.

Example: "sphinx of black quartz judge my vow" should output as "vow my judge quartz black of sphinx"
'''

def reverseWords(self, s: str) -> str:
  words_array = s.split()
  words_array.reverse()
  result = " ".join(words_array)
  return result  

if __name__ == "__main__":
  sentence = "sphinx of black quartz judge my vow"

  result = reverseWords(sentence)
  print(result)