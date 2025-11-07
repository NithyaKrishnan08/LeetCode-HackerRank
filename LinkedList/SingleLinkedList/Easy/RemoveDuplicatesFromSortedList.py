# Remove Duplicates from Sorted List
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
# Leetcode: 83
# Difficulty: Easy

'''
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]

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
    if head is None:
      return None

    temp = head
    while temp and temp.next:
      if temp.val == temp.next.val:
        temp.next = temp.next.next
      else:
        temp = temp.next
    return head
  
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
        