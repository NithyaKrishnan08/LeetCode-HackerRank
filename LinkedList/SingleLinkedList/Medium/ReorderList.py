# Reorder List
# https://leetcode.com/problems/reorder-list/description/
# Leetcode Problem 143: Reorder List
# difficulty: Medium

'''
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Constraints:
The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
'''
from typing import Optional

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def reorderList(self, head: Optional[ListNode]) -> None:
    if not head or not head.next:
      return head
    
    # Step 1: find the middle of the linked list
    slow, fast = head, head
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next

    # Step 2: reverse the second half of the linked list
    prev = None
    curr = slow.next
    slow.next = None
    while curr:
      next_node = curr.next
      curr.next = prev
      prev = curr
      curr = next_node

    # Step 3: merge the two halves
    first = head
    second = prev
    while second:
      temp1 = first.next
      temp2 = second.next

      first.next = second
      second.next = temp1
      first = temp1
      second = temp2

if __name__ == '__main__':
  a = ListNode(1)
  b = ListNode(2)
  c = ListNode(3)
  d = ListNode(4)
  e = ListNode(5)
  f = ListNode(6)
  g = ListNode(7)

  a.next = b
  b.next = c
  c.next = d
  d.next = e
  e.next = f
  f.next = g

  s = Solution()
  s.reorderList(a)

  while a:
    print(a.val, end=' ')
    a = a.next
  print()
        