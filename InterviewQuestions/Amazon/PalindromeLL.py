# Palindrome Linked List
# https://leetcode.com/problems/palindrome-linked-list/description/
# Leetcode Problem 234: Palindrome Linked List

'''
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

 

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
 

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def isPalindrome(self, head: Optional[ListNode]) -> bool:
    if not head or not head.next:
      return True
    
    # Step 1: Find the middle using slow/fast pointers
    slow, fast = head, head
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next

    middle = slow

    # Step 2: Reverse the second half
    temp = middle
    prev = None

    while temp:
      next_node = temp.next
      temp.next = prev
      prev = temp
      temp = next_node

    second_half = prev

    # Step 3: Compare first half and the reversed second half
    temp1, temp2 = head, second_half
    while temp1 and temp2:
      if temp1.val == temp2.val:
        temp1 = temp1.next
        temp2 = temp2.next
      else:
        return False
      
    return True

if __name__ == '__main__':
  s = Solution()
  head = ListNode(1)
  head.next = ListNode(2)
  head.next.next = ListNode(2)
  head.next.next.next = ListNode(1)
  print(s.isPalindrome(head))  # True
        