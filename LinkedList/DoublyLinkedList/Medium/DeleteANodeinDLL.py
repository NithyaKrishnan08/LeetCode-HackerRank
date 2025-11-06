# Delete node in a DLL

class Node:
  def __init__(self, data, next=None, prev=None,):
    self.data = data
    self.next = next
    self.prev = prev

def deleteAtBeginning(head):
  if head is None or head.next is None:
    return None
  
  head = head.next
  head.prev = None

  return head

def deleteAtEnd(head):
  if head is None or head.next is None:
    return None
  
  temp = head
  while temp.next:
    temp = temp.next
  temp.prev.next = None
  
  return head

def deleteAfterGivenNode(head, target):
  if head is None:
    return None
  
  temp = head
  while temp:
    if temp.data == target:
      del_node = temp.next
      if del_node is None:
        return head
      
      next_node = del_node.next
      temp.next = next_node
      if next_node:
        next_node.prev = temp
      return head
      
    temp = temp.next

  return head

def deleteBeforeGivenNode(head, target):
  if head is None or head.next is None:
    return None
  
  temp = head 
  while temp:
    if temp.data == target:
      del_node = temp.prev
      if del_node is None:
        return head
      
      prev_node = del_node.prev
      temp.prev = prev_node
      if prev_node:
        prev_node.next = temp
      else:
        head = temp
      return head
      
    temp = temp.next

  return head

def deleteNodeAtSpecificPosition(head, position):
  if head is None or position <= 0:
    return None
  
  if position == 1:
    return deleteAtBeginning(head)
  
  temp = head
  count = 1

  while temp and count < position:
    temp = temp.next
    count += 1

  if temp is None:
    return head
  
  if temp.next is None:
      return deleteAtEnd(head)

  prev_node = temp.prev
  next_node = temp.next
  
  prev_node.next = next_node
  next_node.prev = prev_node

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
  head.next.next.next = Node(5)
  head.next.next.next.prev = head.next.next
  head.next.next.next.next = Node(6)
  head.next.next.next.next.prev = head.next.next.next
  head.next.next.next.next.next = Node(7)
  head.next.next.next.next.next.prev = head.next.next.next.next

  # Print the original list
  print("Original Linked List:", end='')
  printDLL(head)

  # Delete a node at the front of the list
  # print("After deleting node at the front:", end='')
  # head = deleteAtBeginning(head)
  # printDLL(head)

  # Delete a node at the end of the list
  # print("After deleting node at the end:", end='')
  # head = deleteAtEnd(head)
  # printDLL(head)

  # Delete a node after the given node of the list
  # print("After deleting node after the given node:", end='')
  # head = deleteAfterGivenNode(head, 4)
  # printDLL(head)

  # Delete a node after the given node of the list
  # print("After deleting node before the given node:", end='')
  # head = deleteBeforeGivenNode(head, 4)
  # printDLL(head)

  # Delete a node after the given node of the list
  print("After deleting node at the specific position:", end='')
  head = deleteNodeAtSpecificPosition(head, 3)
  printDLL(head)

  

  

