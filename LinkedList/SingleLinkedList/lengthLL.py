# Insert node at the head of the linked list

class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

# Print the LL - traversal
def countNodesLL(head):
  temp = head
  count = 0
  while temp is not None:
    count += 1
    temp = temp.next
  return count

if __name__ == "__main__":
  arr = [12, 8, 5, 7]
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  result = countNodesLL(head)
  print("Count: ", result)
  

