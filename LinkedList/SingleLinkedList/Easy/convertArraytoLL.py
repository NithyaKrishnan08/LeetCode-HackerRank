# Insert node at the head of the linked list

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

def convertArrayToLL(arr):
  if not arr:
    return None
  head = Node(arr[0])
  mover = head
  for i in range(1, len(arr)):
    temp = Node(arr[i])
    mover.next = temp
    mover = temp
  return head

if __name__ == "__main__":
  arr = [12, 8, 5, 7]
  result = convertArrayToLL(arr)
  print(result.data)

  

