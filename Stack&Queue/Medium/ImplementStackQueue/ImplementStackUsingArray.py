# Implement stack using array
#  IFO - Last In First Out

class Stack:
  def __init__(self):
    self.top = -1
    self.size = 1000
    self.arr = [0] * self.size

  # TC: O(1)
  # SC: O(size)
  def push(self, x: int) -> None:
    self.top += 1
    self.arr[self.top] = x

  # TC: O(1)
  # SC: O(size)
  def pop(self) -> int:
    x = self.arr[self.top]
    self.top -= 1
    return x
  
  # TC: O(1)
  # SC: O(size)
  def Top(self) -> int:
    return self.arr[self.top]
  
  # TC: O(1)
  # SC: O(size)
  def Size(self) -> int:
    return self.top + 1
  
if __name__ == "__main__":
  s = Stack()
  s.push(6)
  s.push(3)
  s.push(7)
  print("Top of stack before deleting any element", s.Top())
  print("Size of stack before deleting any element", s.Size())
  print("The deleted element: ", s.pop())
  print("Size of stack after deleting an element", s.Size())
  print("Top of stack after deleting an element", s.Top())