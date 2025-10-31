# Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/description/
# Leetcode: 141
# Difficulty: Easy

# To detect a cycle in the linked list

class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

# Brute force solution
# Time Complexity : O(N * 2 * log(N))
# Space Complexity : O(N)
def detectLoopLL1(head):
  temp = head
  node_set = set()
  while temp is not None:
    if temp in node_set:
      return True
    node_set.add(temp)
    temp = temp.next
  return False

# Optimal solution - Tortoise Hare Method
# Time Complexity : O(N)
# Space Complexity : O(1)
def detectLoopLL2(head, n):
  slow = head
  fast = head

  while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      return True
  return False

def printLL(head):
  while head is not None:
    print(head.data,end=' ')
    head = head.next
  print()

if __name__ == "__main__":
  head = Node(1)
  second = Node(2)
  third = Node(3)
  fourth = Node(4)
  fifth = Node(5)

  head.next = second
  second.next = third
  third.next = fourth
  fourth.next = fifth
  fifth.next = third

  # result1 = detectLoopLL1(head)
  # print("Brute force solution")
  # print("Loop detected" if result1 else "No loop detected")

  result2 = detectLoopLL1(head)
  print("Optimal solution")
  print("Loop detected" if result2 else "No loop detected")
  

