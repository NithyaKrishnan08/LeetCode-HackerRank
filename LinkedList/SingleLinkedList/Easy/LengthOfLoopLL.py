# Length of cycle in Linked List
# https://www.geeksforgeeks.org/dsa/find-length-of-loop-in-linked-list/
# Difficulty: Easy

'''
Given the head of a singly linked list, determine the length of the cycle (loop) if one exists. A cycle occurs when a node's next pointer points to a previously visited node in the list. If no cycle is present, return 0.

Examples:

Input: 

2-
 
Output: 3
Explanation: There exists a loop in the linked list and the length of the loop is 3. 

Input: 

link1
 
Output: 0
Explanation: There is no loop present in the Linked List.
'''
# Tortoise Hare Method

class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

# Optimal solution - Tortoise Hare Method
# Time Complexity : O(N)
# Space Complexity : O(1)
def LengthofLoopLL(head):
  def countNodes(node):
    count = 1
    temp = node
    while temp.next != node:
      count += 1
      temp = temp.next
    return count
  
  slow = head
  fast = head

  while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      return countNodes(slow)
  
  return 0

def printLL(head):
  while head is not None:
    print(head.data,end=' ')
    head = head.next
  print()

if __name__ == "__main__":
  head = Node(25)
  head.next = Node(14)
  head.next.next = Node(19)
  head.next.next.next = Node(33)
  head.next.next.next.next = Node(10)
  
  head.next.next.next.next.next = head.next.next

  result = LengthofLoopLL(head)
  print(f"Length of Loop: {result}")