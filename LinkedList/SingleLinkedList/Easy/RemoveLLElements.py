# Remove Linked List Elements
# https://leetcode.com/problems/remove-linked-list-elements/description/
# Leetcode Problem 203: Remove Linked List Elements
# Difficulty: Easy

'''
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

 

Example 1:


Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
Example 2:

Input: head = [], val = 1
Output: []
Example 3:

Input: head = [7,7,7,7], val = 7
Output: []
 

Constraints:

The number of nodes in the list is in the range [0, 104].
1 <= Node.val <= 50
0 <= val <= 50
'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    if head is None:
      return head
    
    dummy_node = ListNode(-1)
    dummy_node.next = head
    temp = dummy_node

    while temp and temp.next:
      if temp.next.val == val:
        temp.next = temp.next.next
      else:
        temp = temp.next

    return dummy_node.next
  
if __name__ == '__main__':
  s = Solution()
  head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
  val = 6
  res = s.removeElements(head, val)
  while res:
    print(res.val)
    res = res.next
        