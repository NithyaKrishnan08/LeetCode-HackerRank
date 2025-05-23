# Implement Trie

'''
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
 

Constraints:

1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 104 calls in total will be made to insert, search, and startsWith.
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

class Trie:
  def __init__(self):
    self.root = TrieNode()

  def insert(self, word):
    node = self.root
    for ch in word:
      if ch not in node.children:
        node.children[ch] = TrieNode()
      node = node.children[ch]
    node.is_end = True
  
  def search(self, word):
    node = self.root
    for ch in word:
      if ch not in node.children:
        return False
      node = node.children[ch]
    return node.is_end

  def startsWith(self, prefix):
    node = self.root
    for ch in prefix:
      if ch not in node.children:
        return False
      node = node.children[ch]
    return True


if __name__ == "__main__":
    trie = Trie()
    print("Inserting words: Striver, Striving, String, Strike")
    trie.insert("striver")
    trie.insert("striving")
    trie.insert("string")
    trie.insert("strike")

    print("Search if Strawberry exists in trie: " +
          ("True" if trie.search("strawberry") else "False"))

    print("Search if Strike exists in trie: " +
          ("True" if trie.search("strike") else "False"))

    print("If words in Trie start with Stri: " +
          ("True" if trie.startsWith("stri") else "False"))
                           
                        