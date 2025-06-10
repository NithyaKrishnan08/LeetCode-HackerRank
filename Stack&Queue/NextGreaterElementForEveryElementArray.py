# Next Greater Element (NGE) for every element in the given array

'''
Given an array arr[] of integers, the task is to find the Next Greater Element for each element of the array in order of their appearance in the array.
Note: The Next Greater Element for an element x is the first greater element on the right side of x in the array. Elements for which no greater element exist, consider the next greater element as -1. 

Examples: 

Input: arr[] = [1, 3, 2, 4]
Output: [3, 4, 4, -1]
Explanation: The next larger element to 1 is 3, 3 is 4, 2 is 4 and for 4, since it doesn't exist, it is -1.

Input: arr[] = [6, 8, 0, 1, 3]
Output: [8, -1, 1, 3, -1]
Explanation: The next larger element to 6 is 8, for 8 there is no larger elements hence it is -1, for 0 it is 1 , for 1 it is 3 and then for 3 there is no larger element on right and hence -1.

Input: arr[] = [50, 40, 30, 10]
Output: [-1, -1, -1, -1]
Explanation: There is no greater element for any of the elements in the array, so all are -1.
'''

# TC: O(2N)
# SC: O(2N)
def nextLargerElement(arr):
  n = len(arr)
  nge_arr = [0] * n
  st = []
  
  for i in range(n - 1, -1, -1):
    while st and st[-1] <= arr[i]:
      st.pop()

    if not st:
      nge_arr[i] = -1
    else:
      nge_arr[i] = st[-1]

    st.append(arr[i])

  return nge_arr

if __name__ == "__main__":
  arr = [6, 8, 0, 1, 3]

  res = nextLargerElement(arr)
  print(" ".join(map(str, res)))