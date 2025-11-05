# Reverse Nodes in k-Group
# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
# Leetcode Problem 25: Reverse Nodes in k-Group
# Difficulty: Hard

'''
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
 

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000
'''
from typing import Optional

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head or k == 1:
      return head

    # Reverse helper function
    def reverse(start, end):
      prev = None
      curr = start

      while curr != end:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
        
      return prev
    
    # count total no. of nodes
    n = 0
    temp = head
    while temp:
      n += 1
      temp = temp.next

    dummy = ListNode(-1)
    dummy.next = head
    prev = dummy
    curr = head

    while n >= k:
      tail = curr
      
      # Move to the next group
      for _ in range(k):
        tail = tail.next

      # Reverse the current group
      new_head = reverse(curr, tail)

      # Connect with previous part
      prev.next = new_head
      curr.next = tail

      # Move prev and curr pointers
      prev = curr
      curr = tail
      n -= k

    return dummy.next
  
if __name__ == "__main__":
  # Create a linked list 1 -> 2 -> 3 -> 4 -> 5
  head = ListNode(1)
  head.next = ListNode(2)
  head.next.next = ListNode(3)
  head.next.next.next = ListNode(4)
  head.next.next.next.next = ListNode(5)

  k = 2

  solution = Solution()
  new_head = solution.reverseKGroup(head, k)

  # Print the modified linked list
  temp = new_head
  while temp:
    print(temp.val, end=" -> " if temp.next else "")
    temp = temp.next
  print()