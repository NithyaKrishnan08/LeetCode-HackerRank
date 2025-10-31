# Middle of the Linked List
# https://leetcode.com/problems/middle-of-the-linked-list/
# Leetcode Problem 876: Middle of the Linked List
# Difficulty: Easy

'''
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
'''
from typing import Optional

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    temp = head
    slow, fast = temp, temp

    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next

    return slow
  
if __name__ == '__main__':
  sol = Solution()
  head = ListNode(1)
  head.next = ListNode(2)
  head.next.next = ListNode(3)
  head.next.next.next = ListNode(4)
  head.next.next.next.next = ListNode(5)

  ans = sol.middleNode(head)
  while ans:
    print(ans.val)
    ans = ans.next
    
        