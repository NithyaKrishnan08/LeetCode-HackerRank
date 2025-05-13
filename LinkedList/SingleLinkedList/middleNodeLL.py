# Middle node in the linked list

class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

# Brute force solution
# Time Complexity : O(N + N / 2)
# Space Complexity : O(1)
def middleNodeLL1(head):
  temp = head
  count = 0
  while temp is not None:
    count += 1
    temp = temp.next
  middleNodeCount = (count // 2) + 1

  temp = head
  while temp is not None:
    middleNodeCount -= 1
    if middleNodeCount == 0:
      return temp
    temp = temp.next
  return temp

# Optimal solution - Tortoise Hare Method
# Time Complexity : O(N)
# Space Complexity : O(1)
def middleNodeLL2(head):
  slow = head
  fast = head

  while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next

  return slow

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
  sixth = Node(6)

  head.next = second
  second.next = third
  third.next = fourth
  fourth.next = fifth
  fifth.next = sixth

  # result1 = middleNodeLL1(head)
  # print("Brute force solution")
  # print("Middle node: ",result1.data)

  result2 = middleNodeLL2(head)
  print("Optimal solution")
  print("Middle node: ",result2.data)
  

