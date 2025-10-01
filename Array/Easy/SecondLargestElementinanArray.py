# Second Largest Element in an Array
# In one traversal

class Solution:
  def secondLargest(self, arr):
    n = len(arr)
    if n < 2:
      return -1
    
    largest = second_largest = float('-inf')

    for num in arr:
      if num > largest:
        second_largest = largest
        largest = num
      elif num < largest and num > second_largest:
        second_largest = num

    return second_largest if second_largest != float('-inf') else -1
  
if __name__ == "__main__":
  arr = [12, 35, 1, 10, 34, 1]
  obj = Solution()
  result = obj.secondLargest(arr)
  print(f"Second largest element in the array {arr} is: {result}")
        