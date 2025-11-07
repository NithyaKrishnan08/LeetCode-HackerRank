# Reverse a DLL
# Difficulty: Medium

'''
Given the head of a Doubly Linked List, reverse the list in-place so that the first node becomes the last, the second node becomes the second last, and so on. Return the new head of the reversed list.
'''

class Node:
  def __init__(self, data, next=None, prev=None,):
    self.data = data
    self.next = next
    self.prev = prev

class Solution:
  def reverseDLL(self, head):
    # Base case
    if head is None or head.next is None:
      return head

    temp = head
    prev_node = None

    while temp:
      # Swap prev and next pointers
      temp.prev, temp.next = temp.next, temp.prev
      # Move prev_node to current node before advancing
      prev_node = temp
      # Move to next node (which is now temp.prev after swap)
      temp = temp.prev

    # prev_node is the new head of reversed list
    return prev_node

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
  node3 = Node(4)
  node4 = Node(5)
  node5 = Node(6)
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

  new_head = sol.reverseDLL(head)

  print("Reversed Linked List:", end=' ')
  sol.printDLL(new_head)

  