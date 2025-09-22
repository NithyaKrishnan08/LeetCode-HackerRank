# Remove Loop in Linked List
'''
Given the head of a linked list that may contain a loop.  A loop means that the last node of the linked list is connected back to a node in the same list. The task is to remove the loop from the linked list (if it exists).
'''
# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None
    
class Solution:
  def removeLoop(self, head):
    if not head or not head.next:
      return None
    
    slow, fast = head, head

    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      # Cycle detected
      if slow == fast:
        # To find start of cycle - slow will be start of cycle
        slow = head
        while slow != fast:
          slow = slow.next
          fast = fast.next

        # To find end of cycle
        while fast.next != slow:
          fast = fast.next
        fast.next = None

if __name__ == "__main__":
  solution = Solution()

  head = ListNode(3)
  head.next = ListNode(2)
  head.next.next = ListNode(0)
  head.next.next.next = ListNode(-4)
  head.next.next.next.next = head.next

  solution.removeLoop(head)
  # Print the linked list to verify the loop is removed
  temp = head
  while temp:
    print(temp.val, end=" -> ")
    temp = temp.next
  print("None")