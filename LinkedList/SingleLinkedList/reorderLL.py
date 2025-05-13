# Middle node in the linked list

class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

# Optimal solution - Tortoise Hare Method
# Time Complexity : O(N)
# Space Complexity : O(1)
def middleLL(head):
  slow = head
  fast = head

  while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next

  return slow

def reverseLL(head):
  temp = head
  prev = None
  while temp is not None:
    next_node = temp.next
    temp.next = prev
    prev = temp
    temp = next_node
  return prev

def reorderLL(head):
  if head == None or head.next == None:
    return head
  
  middle = middleLL(head)
  second_half_head = reverseLL(middle.next)
  middle.next = None
  
  temp1 = head
  temp2 = second_half_head
  dummyNode1 = None
  dummyNode2 = None

  while temp1 is not None and temp2 is not None:
    dummyNode1 = temp1.next
    dummyNode2 = temp2.next

    temp1.next = temp2
    temp2.next = dummyNode1

    temp1 = dummyNode1
    temp2 = dummyNode2

  return head

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

  result = reorderLL(head)
  print("Optimal solution")
  print("Reordering of LinkedList")
  printLL(result)
  
  

