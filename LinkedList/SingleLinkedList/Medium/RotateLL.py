# Rotate List
# https://leetcode.com/problems/rotate-list/description/
# Leetcode: 61
# difficulty: Medium

'''
Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head or not head.next or k == 0:
      return head
    
    # Step 1: Find length of linked list
    n = 1
    tail = head
    while tail.next:
      tail = tail.next
      n += 1

    # Step 2: Compute the effective rotations
    k = k % n
    if k == 0:
      return head
    
    # Step 3: Find new tail at n - k - 1 position
    new_tail = head
    for _ in range(n - k - 1):
      new_tail = new_tail.next

    # Step 4: Set new head and rearrange pointers
    new_head = new_tail.next
    new_tail.next = None
    tail.next = head

    return new_head
  
if __name__ == "__main__":
  solution = Solution()

  head = ListNode(1)
  head.next = ListNode(2)
  head.next.next = ListNode(3)
  head.next.next.next = ListNode(4)
  head.next.next.next.next = ListNode(5)
  k = 2

  result = solution.rotateRight(head, k)
  while result:
    print(result.val, end=" -> ")
    result = result.next
  print("None")

  head = ListNode(0)
  head.next = ListNode(1)
  head.next.next = ListNode(2)
  k = 4

  result = solution.rotateRight(head, k)
  while result:
    print(result.val, end=" -> ")
    result = result.next
  print("None")

