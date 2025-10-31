# Reverse Linked List II
# https://leetcode.com/problems/reverse-linked-list-ii/description/
# Leetcode Problem 92: Reverse Linked List II
# Difficulty: Medium
'''
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]
 

Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
'''
from typing import Optional

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    if not head and left == right:
      return head
    
    dummp_node = ListNode(-1)
    dummp_node.next = head
    prev = dummp_node

    # Step 1: Move prev to the node just before left
    for _ in range(left - 1):
      prev = prev.next

    # Step 2: Reverse the sublist from left to right
    temp = prev.next
    prev_1 = None
    for _ in range(right - left + 1):
      next_node = temp.next
      temp.next = prev_1
      prev_1 = temp
      temp = next_node

    # Step 3: Connect the reversed sublist back to the main list
    new_tail = prev.next
    new_head = prev_1
    new_tail.next = temp
    prev.next = new_head

    return dummp_node.next
  
if __name__ == "__main__":
  # Create a linked list 1 -> 2 -> 3 -> 4 -> 5
  head = ListNode(1)
  head.next = ListNode(2)
  head.next.next = ListNode(3)
  head.next.next.next = ListNode(4)
  head.next.next.next.next = ListNode(5)

  left = 2
  right = 4

  solution = Solution()
  new_head = solution.reverseBetween(head, left, right)

  # Print the modified linked list
  temp = new_head
  while temp:
    print(temp.val, end=" -> " if temp.next else "")
    temp = temp.next
  print()


    
        