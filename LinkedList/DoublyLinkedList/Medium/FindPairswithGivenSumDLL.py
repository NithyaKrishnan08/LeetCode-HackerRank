# Find pairs with given sum in doubly linked list

'''
Given a sorted doubly linked list of positive distinct elements, the task is to find pairs in a doubly-linked list whose sum is equal to the given value x in sorted order.

Examples:
Input:
Find-pairs-with-given-sum-in-doubly-linked-list
Output: (1, 6), (2,5)
Explanation: We can see that there are two pairs (1, 6) and (2, 5) with sum 7.

Input: 
Find-pairs-with-given-sum-in-doubly-linked-list-2
Output: (1,5)
Explanation: We can see that there is one pair (1, 5) with a sum of 6.
'''
class Node:
  def __init__(self, data, next=None, prev=None,):
    self.data = data
    self.next = next
    self.prev = prev

class Solution:
  def findSumPairsDLL(self, head, target):
    if head is None:
      return None
    
    right = head
    while right.next:
      right = right.next

    left = head
    pairs = []
    while left != right and right.next != left:
      curr_sum = left.data + right.data
      if curr_sum == target:
        pairs.append((left.data, right.data))
        left = left.next
        right = right.prev
      elif curr_sum < target:
        left = left.next
      else:
        right = right.prev
    
    return pairs
  

if __name__ == "__main__":
  head = Node(1)
  head.next = Node(2)
  head.next.prev = head
  head.next.next = Node(4)
  head.next.next.prev = head.next
  head.next.next.next = Node(5)
  head.next.next.next.prev = head.next.next
  head.next.next.next.next = Node(6)
  head.next.next.next.next.prev = head.next.next.next
  head.next.next.next.next.next = Node(8)
  head.next.next.next.next.next.prev = head.next.next.next.next
  head.next.next.next.next.next.next = Node(9)
  head.next.next.next.next.next.next.prev = head.next.next.next.next.next

  sol = Solution()
  pairs = sol.findSumPairsDLL(head, target=7)
  for pair in pairs:
    print(pair)
    
