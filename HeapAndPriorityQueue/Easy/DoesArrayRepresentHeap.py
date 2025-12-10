# does array represent a heap

class Solution:
  def is_min_heap(self, arr):
    n = len(arr)
    for i in range(n // 2):
      left = 2 * i + 1
      right = 2 * i + 2

      if left < n and arr[i] > arr[left]:
        return False
      if right < n and arr[i] > arr[right]:
        return False
      
    return True
  
  def is_max_heap(self, arr):
    n = len(arr)
    for i in range(n // 2):
      left = 2 * i + 1
      right = 2 * i + 2

      if left < n and arr[i] < arr[left]:
        return False
      if right < n and arr[i] < arr[right]:
        return False
      
    return True
  
if __name__ == "__main__":
  solution = Solution()

  arr_min_heap = [-4, 0, 1, 3, 2, 5, 10, 8, 12, 9]
  is_min_heap = solution.is_min_heap(arr_min_heap)
  print(f"The array {arr_min_heap} represents a Min Heap: {is_min_heap}")

  arr_max_heap = [90, 15, 10, 7, 12, 2]
  is_max_heap = solution.is_max_heap(arr_max_heap)
  print(f"The array {arr_max_heap} represents a Max Heap: {is_max_heap}")