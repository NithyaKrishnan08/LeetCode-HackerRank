# Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/description/
# Leetcode: 23
# Difficulty: Hard

'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []

Constraints:
k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
'''

from typing import List, Optional
from queue import PriorityQueue

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    pq = PriorityQueue()

    for idx, node in enumerate(lists):
      if node:
        pq.put((node.val, idx, node))

    dummy = ListNode(-1)
    temp = dummy

    while not pq.empty():
      _, idx, current_node = pq.get()

      if current_node.next:
        pq.put((current_node.next.val, idx, current_node.next))

      temp.next = current_node
      temp = temp.next

    return dummy.next
  
if __name__ == "__main__":
  head1 = ListNode(2, ListNode(4, ListNode(6)))
  head2 = ListNode(1, ListNode(5))
  head3 = ListNode(1, ListNode(1, ListNode(3, ListNode(7))))
  head4 = ListNode(8)

  lists = [head1, head2, head3, head4]

  solution = Solution()
  merged_head = solution.mergeKLists(lists)

  while merged_head is not None:
    print(merged_head.val,end=' ')
    merged_head = merged_head.next
  print()
