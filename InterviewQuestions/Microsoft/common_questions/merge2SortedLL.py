'''
Problem Statement: Write a function that takes two sorted linked lists and merges them. The function should return a single, sorted list made from splicing the nodes of the first two lists together.

For example, if the first linked list is 1 -> 2 -> 4 and the second linked list is 3 -> 5 -> 6, then the output would be 1 -> 2 -> 3 -> 4 -> 5 -> 6
'''
class Node:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

def merge2SortedLL2(list1, list2):
  temp1 = list1
  temp2 = list2
  dummy_node = Node(-1)
  temp = dummy_node

  while temp1 is not None and temp2 is not None:
    if temp1.val <= temp2.val:
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

    return dummy_node.next