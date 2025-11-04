# Add Two Numbers II
# https://leetcode.com/problems/add-two-numbers-ii/description/
# Leetcode Problem 445: Add Two Numbers II
# Difficulty: Medium

'''
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]
Example 2:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]
Example 3:

Input: l1 = [0], l2 = [0]
Output: [0]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

'''
from typing import Optional

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    def reverseLL(node):
      if not node:
        return node
      
      temp = node
      prev = None

      while temp:
        next_node = temp.next
        temp.next = prev
        prev = temp
        temp = next_node

      return prev
    
    # Step 1: Reverse both LLs
    l1 = reverseLL(l1)
    l2 = reverseLL(l2)

    # Step 2: Add the two numbers
    carry = 0
    head = None

    while l1 or l2 or carry:
      val1 = l1.val if l1 else 0
      val2 = l2.val if l2 else 0

      total = val1 + val2 + carry
      carry = total // 10
      new_node = ListNode(total % 10)

      new_node.next = head
      head = new_node

      if l1:
        l1 = l1.next
      if l2:
        l2 = l2.next

    return head
  

if __name__ == '__main__':
  sol = Solution()

  l1 = ListNode(7)
  l1.next = ListNode(2)
  l1.next.next = ListNode(4)
  l1.next.next.next = ListNode(3)

  l2 = ListNode(5)
  l2.next = ListNode(6)
  l2.next.next = ListNode(4)

  result = sol.addTwoNumbers(l1, l2)

  while result:
    print(result.val, end=' -> ')
    result = result.next
  print('None')