# Implement Queue using arrays
# FIFO - First In First Out

class Queue:
  def __init__(self):
    self.start = -1
    self.end = -1
    self.cur_size = 0
    self.max_size = 10
    self.arr = [0] * self.max_size


  # TC: O(1)
  # SC: O(N) 
  def push(self, x: int) -> None:
    if self.cur_size == self.max_size:
      print("Queue is full!")
      exit(1)
    if self.cur_size == 0:
      self.start = 0
      self.end = 0
    else:
      self.end = (self.end + 1) % self.max_size

    self.arr[self.end] = x
    print(f"The element {x} is pushed")
    self.cur_size += 1

  # TC: O(1)
  # SC: O(N)
  def pop(self) -> int:
    if self.start == -1:
      print("Queue is empty")
    popped = self.arr[self.start]
    if self.cur_size == -1:
      self.start = -1
      self.end = -1
    else:
      self.start = (self.start + 1) % self.max_size

    return popped
  
  # TC: O(1)
  # SC: O(N)
  def Top(self) -> int:
    if self.cur_size == 0:
      print("Queue is empty")
    return self.arr[self.start]
  
  # TC: O(1)
  # SC: O(N)
  def Size(self) -> int:
    return self.cur_size
  
if __name__ == "__main__":
  q = Queue()
  q.push(6)
  q.push(3)
  q.push(7)
  print("Top of queue before deleting any element", q.Top())
  print("Size of queue before deleting any element", q.Size())
  print("The deleted element: ", q.pop())
  print("Size of queue after deleting an element", q.Size())
  print("Top of queue after deleting an element", q.Top())