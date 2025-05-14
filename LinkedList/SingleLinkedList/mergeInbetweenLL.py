# Merge in between linked lists
'''
You are given two linked lists: list1 and list2 of sizes n and m respectively.

Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

The blue edges and nodes in the following figure indicate the result:


Build the result list and return its head.
'''

class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

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

# Brute force solution
# Time Complexity : O(N1 + N2) + O(N log N) + O(N) -> N : N1 + N2
# Space Complexity : O(N)+O(N)
def mergeInBetween(list1, a: int, b: int, list2):
  if not list1 or not list2:
    return list1
  
  temp1 = list1
  temp2 = list2
  count = -1

  while temp1 is not None:
    count += 1
    if count == a - 1:
      node1 = temp1
    if count == b:
      node2 = temp1.next
    temp1 = temp1.next
  
  node1.next = temp2
  while temp2.next is not None:
    temp2 = temp2.next
  temp2.next = node2
  
  return list1

def printLL(head):
  while head is not None:
    print(head.data,end=' ')
    head = head.next
  print()

if __name__ == "__main__":
  list1 = Node(10)
  list1.next = Node(1)
  list1.next.next = Node(13)
  list1.next.next.next = Node(6)
  list1.next.next.next.next = Node(9)
  list1.next.next.next.next.next = Node(5)

  list2 = Node(1000000)
  list2.next = Node(1000001)
  list2.next.next = Node(1000002)

  a = 3
  b = 4

  result2 = mergeInBetween(list1, a, b, list2)
  print("Optimal solution")
  printLL(result2)
  

