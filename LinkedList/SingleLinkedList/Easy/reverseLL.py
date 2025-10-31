# Reverse the linked list
# https://leetcode.com/problems/reverse-linked-list/description/
# Leetcode Problem 206: Reverse Linked List
# Difficulty: Easy

'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

def reverseLL(head):
  temp = head
  prev = None
  while temp is not None:
    next_node = temp.next
    temp.next = prev
    prev = temp
    temp = next_node
  return prev

def printLL(head):
  while head is not None:
    print(head.data,end=' ')
    head = head.next
  print()

if __name__ == "__main__":
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  result = reverseLL(head)
  printLL(result)
  

