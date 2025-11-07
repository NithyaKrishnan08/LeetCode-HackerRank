# Remove Duplicates from Sorted List II
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
# Leetcode: 82
# Difficulty: Medium

'''
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:
Input: head = [1,1,1,2,3]
Output: [2,3]

Constraints:
The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    curr = head

    while curr:
      # Check for duplicates
      if curr.next and curr.val == curr.next.val:
        # Skip all nodes with the same value
        while curr.next and curr.val == curr.next.val:
          curr = curr.next
        # Link previous distinct node to the next distinct node
        prev.next = curr.next
      else:
        prev = prev.next
      
      curr = curr.next

    return dummy.next
    
  
if __name__ == '__main__':
  s = Solution()
  head = ListNode(1)
  head.next = ListNode(1)
  head.next.next = ListNode(2)
  head.next.next.next = ListNode(3)
  head.next.next.next.next = ListNode(3)

  res = s.deleteDuplicates(head)
  while res:
    print(res.val, end=" -> " if res.next else "")
    res = res.next
  print()
        