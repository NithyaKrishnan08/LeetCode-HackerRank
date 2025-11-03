# Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
# Leetcode: 19
# Difficulty: Medium

class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

# Brute force solution
# Time Complexity : O(length of LL) + O(length of LL - n)
# Space Complexity : O(1)
def removeNthNodeFromEndLL1(head, n):
  temp = head
  total_nodes = 0
  while temp is not None:
    total_nodes += 1
    temp = temp.next

  if total_nodes == n:
    new_head = head.next
    return new_head
  
  temp = head
  result = total_nodes - n
  while temp is not None:
    result -= 1
    if result == 0:
      delete_node = temp.next
      temp.next = delete_node.next
      break
    temp = temp.next
  return head

# Optimal solution
# Time Complexity : O(length of LL)
# Space Complexity : O(1)
def removeNthNodeFromEndLL2(head, n):
  fast = head
  for _ in range(n):
    fast = fast.next

  if not fast:
    new_head = head.next
    return new_head

  slow = head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next

  delete_node = slow.next
  slow.next = delete_node.next

  return head

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
  head.next.next.next.next.next = Node(6)

  # result1 = removeNthNodeFromEndLL1(head, 2)
  # print("Brute force solution")
  # printLL(result1)

  result2 = removeNthNodeFromEndLL2(head, 2)
  print("Optimal solution")
  printLL(result2)
  

