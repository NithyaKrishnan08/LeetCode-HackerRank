# Reverse a stack using recursion

'''
Given a stack st[], Reverse the stack so that the top element becomes the bottom and the bottom element becomes the top, while preserving the order of the remaining elements accordingly.

Example 1: 
Input: st[] = [1, 2, 3, 4]
Output: [1, 2, 3, 4]

Example 2:
Input: st[] = [3, 2, 1]
Output: [3, 2, 1]
'''

class Solution:
  def insertAtBottom(self, st, element):
    if not st:
      st.append(element)
      return
    
    top = st.pop()
    self.insertAtBottom(st, element)

    st.append(top)

  def reverseStack(self, st):
    if not st:
      return
    
    top = st.pop()
    self.reverseStack(st)

    self.insertAtBottom(st, top)


if __name__ == "__main__":
  st = [41, 3, 32, 2, 11]
  solution = Solution()
  solution.reverseStack(st)
  print(st)  # Output should be [41, 32, 11, 3, 2]
