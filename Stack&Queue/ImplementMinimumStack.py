# Implement Minimum Stack

'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 

Constraints:

-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.
'''

class MinStack:
  def __init__(self):
    self.stack = []
    self.minimum = float('inf')

  def push(self, val: int) -> None:
    if not self.stack:
      self.minimum = val
      self.stack.append(val)
    else:
      if val >= self.minimum:
        self.stack.append(val)
      else:
        self.stack.append(2 * val - self.minimum)
        self.minimum = val

  def pop(self) -> None:
    if not self.stack:
      return

    popped = self.stack.pop()
    if popped < self.minimum:
      self.minimum = 2 * self.minimum - popped

  def top(self) -> int:
    if not self.stack:
      return None
    top = self.stack[-1]
    return top if top >= self.minimum else self.minimum

  def getMin(self) -> int:
    return self.minimum if self.stack else None