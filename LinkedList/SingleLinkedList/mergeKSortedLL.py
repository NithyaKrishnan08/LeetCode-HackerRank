# Merge k sorted linked lists
import queue

class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

def convertArrayToLL(arr):
  head = Node(arr[0])
  mover = head
  for i in range(1, len(arr)):
    temp = Node(arr[i])
    mover.next = temp
    mover = temp
  return head

def merge2SortedLL(list1, list2):
  temp1 = list1
  temp2 = list2
  dummyNode = Node(-1)
  temp = dummyNode
  
  while temp1 is not None and temp2 is not None:
    if temp1.data <= temp2.data:
      temp.next = temp1
      temp1 = temp1.next
    else:
      temp.next = temp2
      temp2 = temp2.next
    temp = temp.next

  if temp1 is not None:
    temp.next = temp1
  elif temp2 is not None:
    temp.next = temp2

  return dummyNode.next

# Better solution
# Time Complexity : O( N*k(k+1)/2) ~ O(N*k^2)
# Space Complexity : O(1)

def mergekSortedLL1(listArray):
  head = listArray[0]

  for i in range(1, len(listArray)):
    head = merge2SortedLL(head, listArray[i])
  return head

# Optimized solution
# Time Complexity : O( N*k(k+1)/2) ~ O(N*k^2)
# Space Complexity : O(1)

def mergekSortedLL2(listArray):
  pq = queue.PriorityQueue()

  for node in listArray:
    if node:
      pq.put((node.data, node))

  dummyNode = Node(-1)
  temp = dummyNode

  while not pq.empty():
    _, current_node = pq.get()

    if current_node.next:
      pq.put((current_node.next.data, current_node.next))

    temp.next = current_node
    temp = temp.next

  return dummyNode.next

def printLL(head):
  while head is not None:
    print(head.data,end=' ')
    head = head.next
  print()

if __name__ == "__main__":
  head1 = Node(2, Node(4, Node(6)))
  head2 = Node(1, Node(5))
  head3 = Node(1, Node(1, Node(3, Node(7))))
  head4 = Node(8)

  lists = [head1, head2, head3, head4]

  mergedList = mergekSortedLL1(lists)
  printLL(mergedList)

  # result2 = merge2SortedLL2(list1, list2)
  # print("Optimal solution")
  # printLL(result2)
  

