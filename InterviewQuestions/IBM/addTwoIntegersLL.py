# Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/description/
# Leetcode: 2

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
class ListNode:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

def addTwoNumbersLL(l1, l2):
  dummy_node = ListNode(-1)
  temp = dummy_node
  carry = 0

  while l1 or l2 or carry:
    sum = carry
    if l1:
      sum += l1.val
      l1 = l1.next
    if l2:
      sum += l2.val
      l2 = l2.next

    carry = sum // 10
    node = ListNode(sum % 10)
    temp.next = node
    temp = temp.next

  return dummy_node.next