# Selection sorting
# Time comlpexity: O(n^2)
# Space Complexity: O(1)

def selection_sort(arr):
  n = len(arr)
  for i in range(n):
    min_index = i
    for j in range(i + 1, n):
      if arr[j] < arr[min_index]:
        min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
  
  return arr

if __name__ == "__main__":
  arr = [9, 4, 5, 3, 2, 8, 1, 7, 6]
  
  print("Original array: ", arr)
  sorted_arr = selection_sort(arr)
  print("Sorted array: ", sorted_arr)