# Insert node at the head of the linked list

class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

def deleteLastNodeLL(head):
  temp = head
  while temp is not None:
    if temp.next.next is None:
      temp.next = None
    temp = temp.next
  return head

def printLL(head):
  while head is not None:
    print(head.data, end=' ')
    head = head.next
  print()

if __name__ == "__main__":
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  result = deleteLastNodeLL(head)
  printLL(result)
  

