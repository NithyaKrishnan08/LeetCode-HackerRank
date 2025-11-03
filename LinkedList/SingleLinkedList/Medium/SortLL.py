# Sort List
# https://leetcode.com/problems/sort-list/description/
# Leetcode: 148
# Difficulty: Medium

'''
Given the head of a linked list, return the list after sorting it in ascending order.

 

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105

'''
from typing import Optional

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
      return head
    
    # Step 1: Split the list into two halves
    slow, fast = head, head.next
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next

    mid = slow.next
    slow.next = None # Split the list

    # Step 2: Sort each half recursively
    left = self.sortList(head)
    right = self.sortList(mid)

    # Step 3: Merge the two sorted halves
    return self.merge(left, right)
  
  def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
      if l1.val < l2.val:
        tail.next = l1
        l1 = l1.next
      else:
        tail.next = l2
        l2 = l2.next
      tail = tail.next

    tail.next = l1 if l1 else l2

    return dummy.next


if __name__ == '__main__':
  # Create example linked list: [4, 2, 1, 3]
  head = ListNode(4)
  head.next = ListNode(2)
  head.next.next = ListNode(1)
  head.next.next.next = ListNode(3)

  sol = Solution()
  new_head = sol.sortList(head)

  # Print sorted linked list
  temp = new_head
  while temp:
    print(temp.val, end=" -> " if temp.next else "")
    temp = temp.next
  print()