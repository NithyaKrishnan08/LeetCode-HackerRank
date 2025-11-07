# Delete all occurences of key in DLL
# Difficulty: Medium

'''
You are given the head_ref of a doubly Linked List and a Key. Your task is to delete all occurrences of the given key if it is present and return the new DLL.

Example1:

Input: 
2<->2<->10<->8<->4<->2<->5<->2
2
Output: 
10<->8<->4<->5
Explanation: 
All Occurences of 2 have been deleted.

Example2:

Input: 
9<->1<->3<->4<->5<->1<->8<->4
9
Output: 
1<->3<->4<->5<->1<->8<->4
Explanation: 
All Occurences of 9 have been deleted.
'''
class Node:
  def __init__(self, data, next=None, prev=None,):
    self.data = data
    self.next = next
    self.prev = prev

class Solution:
  def deleteAllKeyDLL(self, head, key):
    if head is None:
      return None

    temp = head
    # Move head to the first node that is not the key
    while temp and temp.data == key:
      temp = temp.next
    if temp:
      temp.prev = None
    head = temp

    # Traverse and delete all occurences of key
    while temp:
      if temp.data == key:
        prev_node = temp.prev
        next_node = temp.next

        if prev_node:
          prev_node.next = next_node
        if next_node:
          next_node.prev = prev_node
        
      temp = temp.next

    return head
  
  # Print the LL
  def printDLL(self, head):
    while head is not None:
      print(head.data, end=' ')
      head = head.next
    print()
  
if __name__ == '__main__':
  sol = Solution()

  head = Node(2)
  node2 = Node(3)
  node3 = Node(2)
  node4 = Node(5)
  node5 = Node(2)
  node6 = Node(7)

  head.next = node2
  node2.prev = head
  node2.next = node3
  node3.prev = node2
  node3.next = node4
  node4.prev = node3
  node4.next = node5
  node5.prev = node4
  node5.next = node6
  node6.prev = node5

  print("Original Linked List:", end=' ')
  sol.printDLL(head)

  new_head = sol.deleteAllKeyDLL(head, key=2)

  print("Reversed Linked List:", end=' ')
  sol.printDLL(new_head)



