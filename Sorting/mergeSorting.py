# Merge Sort
# Divide and Merge
# Time Complexity: O(n log n)
# Space Complexity: O(n)

class Solution:
  def mergeSort(self, arr):
    n = len(arr)

    def merge(arr, low, middle, high):
      temp = []
      left = low
      right = middle + 1

      while left <= middle and right <= high:
        if arr[left] <= arr[right]:
          temp.append(arr[left])
          left += 1
        else:
          temp.append(arr[right])
          right += 1
      
      while left <= middle:
        temp.append(arr[left])
        left += 1

      while right <= high:
        temp.append(arr[right])
        right += 1

      for i in range(len(temp)):
        arr[low + i] = temp[i]

    def merge_sort(arr, low, high):
      if low >= high:
        return
      
      middle = (low + high) // 2
      merge_sort(arr, low, middle)
      merge_sort(arr, middle + 1, high)
      merge(arr, low, middle, high)

    merge_sort(arr, 0, n - 1)

if __name__ == "__main__":
  arr = [38, 27, 43, 3, 9, 82, 10]
  solution = Solution()
  solution.mergeSort(arr)
  print("Sorted array is:", arr)
