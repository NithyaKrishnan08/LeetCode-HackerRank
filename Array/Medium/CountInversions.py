# Count Inversions

'''
The inversion count of an array denotes how far is the array from being sorted.

If the array is sorted, inversion count is 0. If the array is sorted in reverse order, the inversion count is maximum.

More formally, the inversion count of an array A is the number of pairs (i, j) such A[i] < A[j] and i > j.

Example
Lets take the following array:
8, 4, 1, 2

This array has an inversion count of 5.
(8, 4), (8, 1), (8, 2), (4, 1), (4, 2)

Given an array A, calculate the inversion count of the array.
'''

class Solution:
  # Time Complexity: O(n^2)
  # Space Complexity: O(1)
  def countInversionsBrute(self, arr):
    n = len(arr)
    count = 0

    for i in range(n):
      for j in range(i + 1, n):
        if arr[i] > arr[j]:
          count += 1
    
    return count
  
  # Time Complexity: O(n log n)
  # Space Complexity: O(1)
  def countInversions(self, arr):
    n = len(arr)

    def merge(arr, low, middle, high):
      temp = []
      left = low
      right = middle + 1

      count = 0

      while left <= middle and right <= high:
        if arr[left] <= arr[right]:
          temp.append(arr[left])
          left += 1
          # Right is smaller
        else:
          temp.append(arr[right])
          count += (middle - left + 1)
          right += 1
      
      while left <= middle:
        temp.append(arr[left])
        left += 1

      while right <= high:
        temp.append(arr[right])
        right += 1

      for i in range(len(temp)):
        arr[low + i] = temp[i]

      return count

    def merge_sort(arr, low, high):
      if low >= high:
        return 0
      
      count = 0
      
      middle = (low + high) // 2
      count += merge_sort(arr, low, middle)
      count += merge_sort(arr, middle + 1, high)
      count += merge(arr, low, middle, high)
      return count

    return merge_sort(arr, 0, n - 1)
  
if __name__ == "__main__":
  arr = [8, 4, 1, 2]
  solution = Solution()
  print("Inversion count is:", solution.countInversionsBrute(arr))

  print("Inversion count is:", solution.countInversions(arr))