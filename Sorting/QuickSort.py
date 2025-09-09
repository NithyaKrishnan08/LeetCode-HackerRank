# Quick Sort - Ascending Order
# Divide and Conquer
# Time Complexity: O(n log n)
# Space Complexity: O(1)

# Step 1: Pick a pivot element and place it at its correct position in the sorted array.
# Step 2: Place all smaller elements to the left of the pivot and all larger elements to the right of the pivot.
# Step 3: Recursively apply the above steps to the left and right subarrays.

class Solution:
  def quickSortAscending(self, arr):
    n = len(arr)
    low = 0
    high = n - 1

    def findPartion(arr, low, high):
      pivot = arr[low]
      i, j = low, high

      while i < j:
        while i <= high and arr[i] <= pivot:
          i += 1
        while j >= low and arr[j] > pivot:
          j -= 1
        if i < j:
          arr[i], arr[j] = arr[j], arr[i]

      arr[low], arr[j] = arr[j], arr[low]
      return j

    def qs(arr, low, high):
      if low < high:
        partition_index = findPartion(arr, low, high)
        qs(arr, low, partition_index - 1)
        qs(arr, partition_index + 1, high)

    qs(arr, low, high)
    return arr
  
  def quickSortDescending(self, arr):
    n = len(arr)
    low = 0
    high = n - 1

    def findPartion(arr, low, high):
      pivot = arr[low]
      i, j = low, high

      while i < j:
        while i <= high and arr[i] >= pivot:
          i += 1
        while j >= low and arr[j] < pivot:
          j -= 1
        if i < j:
          arr[i], arr[j] = arr[j], arr[i]

      arr[low], arr[j] = arr[j], arr[low]
      return j

    def qs(arr, low, high):
      if low < high:
        partition_index = findPartion(arr, low, high)
        qs(arr, low, partition_index - 1)
        qs(arr, partition_index + 1, high)

    qs(arr, low, high)
    return arr

if __name__ == "__main__":
  arr = [38, 27, 43, 3, 9, 82, 10]
  solution = Solution()
  solution.quickSortAscending(arr)
  print("Sorted array is:", arr)

  arr = [38, 27, 43, 3, 9, 82, 10]
  solution.quickSortDescending(arr)
  print("Sorted array is:", arr)

