# Merge k sorted linked lists
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

import queue

class ListNode:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

def convertArrayToLL(arr):
  head = ListNode(arr[0])
  mover = head
  for i in range(1, len(arr)):
    temp = ListNode(arr[i])
    mover.next = temp
    mover = temp
  return head

def merge2SortedLL(list1, list2):
  temp1 = list1
  temp2 = list2
  dummyNode = ListNode(-1)
  temp = dummyNode
  
  while temp1 is not None and temp2 is not None:
    if temp1.data <= temp2.data:
      temp.next = temp1
      temp1 = temp1.next
    else:
      temp.next = temp2
      temp2 = temp2.next
    temp = temp.next

  if temp1 is not None:
    temp.next = temp1
  elif temp2 is not None:
    temp.next = temp2

  return dummyNode.next

# Better solution
# Time Complexity : O( N*k(k+1)/2) ~ O(N*k^2)
# Space Complexity : O(1)


def mergekSortedLL1(listArray):
  head = listArray[0]

  for i in range(1, len(listArray)):
    head = merge2SortedLL(head, listArray[i])
  return head

# Optimized solution
# Time Complexity : O( N*k(k+1)/2) ~ O(N*k^2)
# Space Complexity : O(1)
from collections import PriorityQueue

def mergekSortedLL2(listArray):
  
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

def printLL(head):
  while head is not None:
    print(head.data,end=' ')
    head = head.next
  print()

if __name__ == "__main__":
  head1 = Node(2, Node(4, Node(6)))
  head2 = Node(1, Node(5))
  head3 = Node(1, Node(1, Node(3, Node(7))))
  head4 = Node(8)

  lists = [head1, head2, head3, head4]

  mergedList = mergekSortedLL2(lists)
  printLL(mergedList)

  # result2 = merge2SortedLL2(list1, list2)
  # print("Optimal solution")
  # printLL(result2)
  

