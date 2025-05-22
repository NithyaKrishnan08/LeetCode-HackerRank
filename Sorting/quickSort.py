# Quick sorting
# Time comlpexity: O(n log n)
# Space Complexity: O(1)

'''
1. Pick a pivot element from the array and place it in the sorted array
2. Smaller numbers on the left and larger elements on the right
3. Recursively apply the above steps to the left and right sub-arrays
'''

def quick_sort(arr):
  n = len(arr)
  for i in range(n):
    min_index = i
    for j in range(i + 1, n):
      if arr[j] < arr[min_index]:
        min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
  
  return arr

if __name__ == "__main__":
  arr = [4, 6, 2, 5, 7, 9, 1, 3]
  
  print("Original array: ", arr)
  sorted_arr = quick_sort(arr)
  print("Sorted array: ", sorted_arr)