# LFU Cache

'''
Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

LFUCache(int capacity) Initializes the object with the capacity of the data structure.
int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.

The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

Explanation
// cnt(x) = the use counter for key x
// cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // return 1
                 // cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                 // cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                 // cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // return 4
                 // cache=[4,3], cnt(4)=2, cnt(3)=3
 

Constraints:

1 <= capacity <= 104
0 <= key <= 105
0 <= value <= 109
At most 2 * 105 calls will be made to get and put.
'''

class Node:
  def __init__(self, key, value, freq = 1, next=None, prev=None):
    self.key = key
    self.value = value
    self.freq = freq
    self.next = next
    self.prev = prev

class DoublyLinkedList:
  def __init__(self):
    self.head = Node(0, 0)
    self.tail = Node(0, 0)
    self.head.next = self.tail
    self.tail.prev = self.head

  def is_empty(self):
    return self.head.next == self.tail
  
  # Most recently used - Insert node before the tail
  def append(self, node):
    node.prev = self.tail.prev
    node.next = self.tail
    self.tail.prev.next = node
    self.tail.prev = node

  # Remove a node
  def remove(self, node):
    node.prev.next = node.next
    node.next.prev = node.prev

  # Remove and return least recently used node
  def pop_left(self):
    if self.is_empty():
      return None
    node = self.head.next
    self.remove(node)
    return node

class LFUCache:
  def __init__(self, capacity: int):
    self.capacity = capacity
    self.size = 0
    self.min_freq = 0
    self.key_table = {} # {key: value}
    self.freq_table = {} # {freq: DLL}

  def update_freq(self, node):
    freq = node.freq
    self.freq_table[freq].remove(node)

    # Clean up if list becomes empty
    if self.freq_table[freq].is_empty():
      del self.freq_table[freq]
      if self.min_freq == freq:
        self.min_freq += 1

    # Update the node frequency
    node.freq += 1
    new_freq = node.freq
    if new_freq not in self.freq_table:
      self.freq_table[new_freq] = DoublyLinkedList()
    self.freq_table[new_freq].append(node)

  def get(self, key: int) -> int:
    if key not in self.key_table:
      return -1
    node = self.key_table[key]
    self.update_freq(node)
    return node.value
      

  def put(self, key: int, value: int) -> None:
    if self.capacity == 0:
      return

    if key in self.key_table:
      node = self.key_table[key]
      node.value = value
      self.update_freq(node)
    else:
      if self.size == self.capacity:
        # Evict least frequently used, least recently used
        list_to_evict = self.freq_table[self.min_freq]
        evict_node = list_to_evict.pop_left()
        del self.key_table[evict_node.key]
        self.size -= 1

      # Insert new node with freq = 1
      new_node = Node(key, value, freq=1)
      self.key_table[key] = new_node
      if 1 not in self.freq_table:
          self.freq_table[1] = DoublyLinkedList()
      self.freq_table[1].append(new_node)
      self.min_freq = 1
      self.size += 1

if __name__ == "__main__":
  lfu = LFUCache(2)
  lfu.put(1, 1)
  lfu.put(2, 2)
  print(lfu.get(1))  # 1
  lfu.put(3, 3)      # Evicts key 2
  print(lfu.get(2))  # -1
  print(lfu.get(3))  # 3
  lfu.put(4, 4)      # Evicts key 1
  print(lfu.get(1))  # -1
  print(lfu.get(3))  # 3
  print(lfu.get(4))  # 4