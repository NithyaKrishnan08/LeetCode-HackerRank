# Insert node in a DLL

class Node:
  def __init__(self, data, next=None, prev=None,):
    self.data = data
    self.next = next
    self.prev = prev

def insertAtBeginning(head, data):
  new_node = Node(data)
  if not head:
    return new_node
  
  new_node.next = head
  head.prev = new_node

  return new_node

def insertAfterGivenNode(head, target, data):
  if head is None:
    return None
  
  temp = head
  while temp:
    if temp.data == target:
      new_node = Node(data)
      new_node.next = temp.next
      new_node.prev = temp

      if temp.next:
        temp.next.prev = new_node
      
      temp.next = new_node
      return head
      
    temp = temp.next

def insertBeforeGivenNode(head, target, data):
  if head is None:
    return None
  
  temp = head
  while temp:
    if temp.data == target:
      new_node = Node(data)
      new_node.prev = temp.prev
      new_node.next = temp
      
      if temp.prev:
        temp.prev.next = new_node
      else:
        head = new_node

      temp.prev = new_node
      return head
      
    temp = temp.next

def insertNodeAtEnd(head, data):
  if head is None:
    return Node(data)
  
  temp = head
  while temp.next:
    temp = temp.next

  new_node = Node(data)
  new_node.prev = temp
  temp.next = new_node

  return head

def insertNodeAtSpecificPosition(head, position, data):
  if head is None:
    return Node(data)
  
  if position == 0:
    return insertAtBeginning(head, data)
  
  temp = head
  for _ in range(position - 1):
    if temp is None:
      break
    temp = temp.next

  if temp is None:
    return insertNodeAtEnd(head, data)

  prev_node = temp.prev
  new_node = Node(data)

  new_node.prev = prev_node
  new_node.next = temp

  prev_node.next = new_node
  temp.prev = new_node

  return head

# Print the LL
def printDLL(head):
  while head is not None:
    print(head.data, end=' ')
    head = head.next
  print()

def convertArrayToDLL(arr):
  head = Node(arr[0])
  mover = head
  for i in range(1, len(arr)):
    temp = Node(arr[i], None, )
    mover.next = temp
    temp.prev = mover
    mover = temp
  return head

if __name__ == "__main__":
  head = Node(2)
  head.next = Node(3)
  head.next.prev = head
  head.next.next = Node(4)
  head.next.next.prev = head.next

  # Print the original list
  print("Original Linked List:", end='')
  printDLL(head)

  # Insert a new node at the front of the list
  print("After inserting Node at the front:", end='')
  data = 1
  head = insertAtBeginning(head, data)

  # Print the updated list
  printDLL(head)

  # Insert a new node after the given node
  print("After inserting Node after target:", end='')
  data = 5
  target = 4
  head = insertAfterGivenNode(head, target, data)

  # Print the updated list
  printDLL(head)

  # Insert a new node before the given node
  print("After inserting Node before target:", end='')
  data = 8
  target = 5
  head = insertBeforeGivenNode(head, target, data)

  # Print the updated list
  printDLL(head)

  # Insert a new node at the end
  print("After inserting Node at the end:", end='')
  data = 7
  head = insertNodeAtEnd(head, data)

  # Print the updated list
  printDLL(head)

  # Insert a new node at the specific position
  print("After inserting Node at the sepcific position:", end='')
  data = 9
  position = 3
  head = insertNodeAtSpecificPosition(head, position, data)

  # Print the updated list
  printDLL(head)

  

