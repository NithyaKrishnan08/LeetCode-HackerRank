# LRU Cache
# https://leetcode.com/problems/lru-cache/
# Leetcode: 146
# Difficulty: Medium

'''
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 

Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
'''
class Node:
  def __init__(self, key, value, next=None, prev=None,):
    self.key = key
    self.value = value
    self.next = next
    self.prev = prev

class LRUCache:
  def __init__(self, capacity: int):
    self.mpp = {}
    self.capacity = capacity
    self.head = Node(-1, -1)
    self.tail = Node(-1, -1)
    self.head.next = self.tail
    self.tail.prev = self.head

  def insertAfterHead(self, new_node):
    temp = self.head.next
    new_node.next = temp
    new_node.prev = self.head
    self.head.next = new_node
    temp.prev = new_node

  def deleteNode(self, del_node):
    prev_node = del_node.prev
    next_node = del_node.next
    prev_node.next = next_node
    next_node.prev = prev_node

  def get(self, key: int) -> int:
    if key not in self.mpp:
      return -1
    
    node = self.mpp[key]
    self.deleteNode(node)
    self.insertAfterHead(node)

    return node.value
      

  def put(self, key: int, value: int) -> None:
    if key in self.mpp:
      node = self.mpp[key]
      node.value = value
      self.deleteNode(node)
      self.insertAfterHead(node)
    else: 
      if len(self.mpp) == self.capacity:
        node = self.tail.prev
        del self.mpp[node.key]
        self.deleteNode(node)
      
      new_node = Node(key, value)
      self.mpp[key] = new_node
      self.insertAfterHead(new_node)

if __name__ == "__main__":
  lru = LRUCache(2)
  lru.put(1, 1)
  lru.put(2, 2)
  print(lru.get(1))    # 1
  lru.put(3, 3)        # Evicts key 2
  print(lru.get(2))    # -1
  lru.put(4, 4)        # Evicts key 1
  print(lru.get(1))    # -1
  print(lru.get(3))    # 3
  print(lru.get(4)) 