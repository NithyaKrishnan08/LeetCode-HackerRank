# Add 1 to a number represented as linked list

'''
A number is represented in linked list such that each digit corresponds to a node in linked list. The task is to add 1 to it.

Examples:

Input: head: 4 -> 5 -> 6
Output: head: 4 -> 5 -> 7
Explanation: Adding 1 to number represented by Linked List = 456 + 1 = 457

nput: head: 2 -> 1 -> 6 -> 9
Output: head:  2 -> 1 -> 7 -> 0
Explanation: Adding 1 to number represented by Linked List = 2169 + 1 = 2170
'''
from typing import Optional

# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def addOne(self, head: ListNode) -> ListNode:
    def reverseLL(node):
      if not head:
        return head
      
      temp = head
      prev = None

      while temp:
        next_node = temp.next
        temp.next = prev
        prev = temp
        temp = next_node

      return prev
    
    # Step 1: Reverse the LL
    head = reverseLL(head)

    # Step 2: Add 1
    carry = 1
    temp = head
    prev = None

    while temp and carry:
      new_val = temp.val + carry
      temp.val = new_val % 10
      carry = new_val // 10
      prev = temp
      temp = temp.next

    # Step 3: If carry remains
    if carry:
      prev.next = ListNode(carry)

    # Step 4: Reverse back the original order
    head = reverseLL(head)

    return head
  

if __name__ == '__main__':
  sol = Solution()

  head = ListNode(2)
  head.next = ListNode(1)
  head.next.next = ListNode(6)
  head.next.next.next = ListNode(9)
  
  new_head = sol.addOne(head)

  # Print the modified linked list
  temp = new_head
  while temp:
    print(temp.val, end=" -> " if temp.next else "")
    temp = temp.next
  print()