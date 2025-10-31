# Insert node at the head of the linked list

class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

# Print the LL - traversal
def searchElementLL(head, target):
  temp = head
  while temp is not None:
    if temp.data == target:
      return True
    temp = temp.next
  return False

if __name__ == "__main__":
  target = 3
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  result = searchElementLL(head, target)
  if result:
    print(f"{target} found in the linked list")
  

