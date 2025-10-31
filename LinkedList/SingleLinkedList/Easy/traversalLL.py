# Insert node at the head of the linked list

class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

# Print the LL - traversal
def printLL(head):
  temp = head
  while temp is not None:
    print(temp.data, end=' ')
    temp = temp.next
  print()

def convertArrayToLL(arr):
  head = Node(arr[0])
  mover = head
  for i in range(1, len(arr)):
    temp = Node(arr[i])
    mover.next = temp
    mover = temp
  return head

if __name__ == "__main__":
  arr = [12, 8, 5, 7]
  

  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print("Traversing the linked list:")
  printLL(head)
  

