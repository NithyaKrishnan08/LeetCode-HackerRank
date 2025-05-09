# Delete last node of the linked list

class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

# Print the LL
def printLL(head):
  while head is not None:
    print(head.data, end=' ')
    head = head.next
  print()

def delete_last_node(head, val):
  new_node = Node(val)
  new_node.next = head
  return new_node

if __name__ == "__main__":
  arr = [12, 8, 5, 7]
  val = 100

  head = Node(arr[0])
  head.next = Node(arr[1])
  head.next.next = Node(arr[2])
  head.next.next.next = Node(arr[3])

  head = insert_at_head(head, val)
  printLL(head)

