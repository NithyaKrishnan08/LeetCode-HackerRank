# Insert node at the head of the linked list

class Node:
  def __init__(self, data, next=None, prev=None,):
    self.data = data
    self.next = next
    self.prev = prev

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
  arr = [12, 8, 5, 7]
  result = convertArrayToDLL(arr)
  printDLL(result)

  

