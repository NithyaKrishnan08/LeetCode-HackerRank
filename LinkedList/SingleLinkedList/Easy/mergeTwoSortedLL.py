# Merge two sorted linked lists
# https://leetcode.com/problems/merge-two-sorted-lists/description/
# Leetcode: 21
# Difficulty: Easy

'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''

class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

def convertArrayToLL(arr):
  head = Node(arr[0])
  mover = head
  for i in range(1, len(arr)):
    temp = Node(arr[i])
    mover.next = temp
    mover = temp
  return head

# Brute force solution
# Time Complexity : O(N1 + N2) + O(N log N) + O(N) -> N : N1 + N2
# Space Complexity : O(N)+O(N)
def merge2SortedLL1(head1, head2):
  temp1 = head1
  temp2 = head2
  arr_list = []

  while temp1 is not None:
    arr_list.append(temp1.data)
    temp1 = temp1.next
  while temp2 is not None:
    arr_list.append(temp2.data)
    temp2 = temp2.next
  
  arr_list.sort()

  result_head = convertArrayToLL(arr_list)
  return result_head

# Optimal solution - Tortoise Hare Method
# Time Complexity : O(N)
# Space Complexity : O(1)
def merge2SortedLL2(list1, list2):
  temp1 = list1
  temp2 = list2
  dummyNode = Node(-1)
  temp = dummyNode
  
  while temp1 and temp2:
    if temp1.data <= temp2.data:
      temp.next = temp1
      temp1 = temp1.next
    else:
      temp.next = temp2
      temp2 = temp2.next
    temp = temp.next

  if temp1:
    temp.next = temp1
  elif temp2:
    temp.next = temp2

  return dummyNode.next

def printLL(head):
  while head is not None:
    print(head.data,end=' ')
    head = head.next
  print()

if __name__ == "__main__":
  list1 = Node(1)
  list1.next = Node(3)
  list1.next.next = Node(5)

  list2 = Node(2)
  list2.next = Node(4)
  list2.next.next = Node(6)

  # result1 = merge2SortedLL1(list1, list2)
  # print("Brute force solution")
  # printLL(result1)

  result2 = merge2SortedLL2(list1, list2)
  print("Optimal solution")
  printLL(result2)
  

