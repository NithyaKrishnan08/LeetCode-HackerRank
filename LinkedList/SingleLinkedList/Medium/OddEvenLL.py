# Odd Even Linked List
# https://leetcode.com/problems/odd-even-linked-list/description/
# Leetcode: 328
# Difficulty: Medium

'''
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity. 

Example 1:
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]

Constraints:
The number of nodes in the linked list is in the range [0, 104].
-106 <= Node.val <= 106
'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
      return head
    
    odd = head
    even = second_head = head.next

    while even and even.next:
      odd.next = even.next
      odd = even.next
      even.next = odd.next
      even = odd.next

    odd.next = second_head

    return head
  

if __name__ == '__main__':
  head = ListNode(2)
  head.next = ListNode(1)
  head.next.next = ListNode(3)
  head.next.next.next = ListNode(5)
  head.next.next.next.next = ListNode(6)
  head.next.next.next.next.next = ListNode(4)
  head.next.next.next.next.next.next = ListNode(7)

  sol = Solution()

  new_head = sol.oddEvenList(head)

  # Print the modified linked list
  temp = new_head
  while temp:
    print(temp.val, end=" -> " if temp.next else "")
    temp = temp.next
  print()

