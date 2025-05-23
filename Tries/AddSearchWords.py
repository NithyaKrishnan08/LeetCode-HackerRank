# Design Add and Search Words Data Structure

'''
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
 

Constraints:

1 <= word.length <= 25
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 2 dots in word for search queries.
At most 104 calls will be made to addWord and search.
'''

# Time Complexity:
# Insertion: O(N)
# Search: O(N)
# Prefix Search: O(N)
# Space Complexity: O(N)
class TrieNode:
  def __init__(self):
    self.children = {}
    self.is_end = False

class WordDictionary:
  def __init__(self):
    self.root = TrieNode()

  def addWord(self, word):
    node = self.root
    for ch in word:
      if ch not in node.children:
        node.children[ch] = TrieNode()
      node = node.children[ch]
    node.is_end = True
  
  def search(self, word):
    def dfs(j, root):
      node = root
      for i in range(j, len(word)):
        ch = word[i]
        if ch == '.':
          for child in node.children.values():
            if dfs(i + 1, child):
              return True
          return False
        else:
          if ch not in node.children:
            return False
          node = node.children[ch]
      return node.is_end
    
    return dfs(0, self.root)



if __name__ == "__main__":
  trie = WordDictionary()
  print("Word \"bad\" is added")
  trie.addWord("bad")

  print("Word \"dad\" is added")
  trie.addWord("dad")
  
  print("Word \"mad\" is added")
  trie.addWord("mad")

  result1 = trie.search("pad")
  if result1:
    print("Word \"pad\" is found in the dictionary")
  else:
    print("Word \"pad\" is not found in the dictionary")

  result2 = trie.search("bad")
  if result2:
    print("Word \"bad\" is found in the dictionary")
  else:
    print("Word \"bad\" is not found in the dictionary")

  result3 = trie.search(".ad")
  if result3:
    print("Word \".ad\" is found in the dictionary")
  else:
    print("Word \".ad\" is not found in the dictionary")
  
  result4 = trie.search("b..")
  if result4:
    print("Word \"b..\" is found in the dictionary")
  else:
    print("Word \"b..\" is not found in the dictionary")

                           
                        