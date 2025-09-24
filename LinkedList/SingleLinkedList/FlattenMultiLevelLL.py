# Flatten a multi-level linked list

'''
You are given a linked list structure, where each node has two pointers:

next: points to an identical node towards the right.
down: points to an identical node towards the bottom.
Only the top most node can have a non-NULL next pointer.

This gives us a set of vertical linked lists and a horizontal linked list with the head nodes of the vertical lists.

Also, all vertical lists are sorted.

Your task is to flatten the lists into a single linked list, which should also be sorted.

'''

# from PIL import Image

# # Open and show image
# img = Image.open("/Users/nithyakrishnan/Desktop/Projects/LeetCode-HackerRank/LinkedList/SingleLinkedList/imageLL/flatten-multi-level-linked-list.png")
# img.show()

from typing import Optional

# Definition for singly-linked list.
class ListNode:
  def __init__(self, data=0, next=None, down=None):
    self.data = data
    self.next = next
    self.down = down

class Solution:
  # TC: O(N + M) + O(N log N) | SC: O(N)
  def flattenLLBrute(self, head: ListNode) -> ListNode:
    arr = []
    temp = head

    while temp != None:
      down = temp
      while down != None:
        arr.append(down.data)
        down = down.down
      temp = temp.next

    arr.sort()
    dummy_node = ListNode(-1)
    temp = dummy_node
    for val in arr:
      temp.down = ListNode(val)
      temp = temp.down
    
    return dummy_node.down

  def flattenLL(self, head: ListNode) -> ListNode:
    def mergeTwoSortedLL(head1: ListNode, head2: ListNode) -> ListNode:
      dummy_node = ListNode(-1)

      temp1 = head1
      temp2 = head2
      temp = dummy_node

      while temp1 and temp2:
        if temp1.data < temp2.data:
          temp.down = temp1
          temp1 = temp1.down
        else:
          temp.down = temp2
          temp2 = temp2.down
        temp = temp.down

      temp.down = temp1 if temp1 else temp2
      return dummy_node.down
    
    if not head or not head.next:
      return head

    head.next = self.flattenLL(head.next)
    head = mergeTwoSortedLL(head, head.next)
    return head 
  
if __name__ == '__main__':
  solution = Solution()

  head = ListNode(5)
  head.down = ListNode(7)
  head.down.down = ListNode(8)
  head.down.down.down = ListNode(30)

  head.next = ListNode(10)
  head.next.down = ListNode(20)

  head.next.next = ListNode(19)
  head.next.next.down = ListNode(22)
  head.next.next.down.down = ListNode(50)

  head.next.next.next = ListNode(28)
  head.next.next.next.down = ListNode(35)
  head.next.next.next.down.down = ListNode(40)
  head.next.next.next.down.down.down = ListNode(45)

  result = solution.flattenLL(head)
  while result:
    print(result.data, end=" -> ")
    result = result.down
  print("None")
  
