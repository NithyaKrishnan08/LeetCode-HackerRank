# Reverse the linked list

class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

def reverseLL(head):
  temp = head
  prev = None
  while temp is not None:
    next_node = temp.next
    temp.next = prev
    prev = temp
    temp = next_node
  return prev

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

  result = reverseLL(head)
  printLL(result)
  

