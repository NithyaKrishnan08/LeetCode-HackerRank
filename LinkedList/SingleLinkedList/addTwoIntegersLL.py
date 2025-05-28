'''
Problem Statement: Given the heads of two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

Examples:

Input Format: 
(Pointer/Access to the head of the two linked lists)

num1  = 243, num2 = 564

l1 = [2,4,3]
l2 = [5,6,4]

Result: sum = 807; L = [7,0,8]

Explanation: Since the digits are stored in reverse order, reverse the numbers first to get the or original number and then add them as → 342 + 465 = 807.
'''
class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

def addTwoNumbersLL(l1, l2):
  dummyNode = Node(-1)
  temp = dummyNode
  carry = 0

  while l1 != None or l2 != None:
    sum = 0
    if l1 != None:
      sum += l1.data
      l1 = l1.next
    if l2 != None:
      sum += l2.data
      l2 = l2.next
    sum += carry
    carry = sum // 10
    node = Node(sum % 10)
    temp.next = node
    temp = temp.next

  return dummyNode.next