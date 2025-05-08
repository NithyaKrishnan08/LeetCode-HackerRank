'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
'''

# Brute Force Solution 
# Time Complexity - O(N^2)
# Space Complexity - O(1))
def maxArea1(height):
  n = len(height)
  maxWater = 0

  for i in range(n):
    for j in range(i + 1, n):
      width = j - i
      minHeight = min(height[i], height[j])
      area = width * minHeight
      maxWater = max(maxWater, area)
  
  return maxWater

# Optimal Solution 
# Time Complexity - O(N)
# Space Complexity - O(1))
def maxArea2(height):
  n = len(height)
  maxWater = 0
  left = 0
  right = n - 1

  while left < right:
    width = right - left
    minHeight = min(height[left], height[right])
    area = width * minHeight
    maxWater = max(maxWater, area)

    if (height[left] < height[right]):
      left += 1
    else:
      right -= 1
  
  return maxWater

if __name__ == "__main__":
  arr1 = [1,8,6,2,5,4,8,3,7]
  arr2 = [1,1]
  
  print("Brute force solution:")
  result1 = maxArea1(arr1)
  print(f"The maximum volume of water in {arr1}: {result1}")

  result2 = maxArea1(arr2)
  print(f"The maximum volume of water in {arr2}: {result2}")

  print("Optimal solution:")
  result3 = maxArea2(arr1)
  print(f"The maximum volume of water in {arr1}: {result1}")

  result4 = maxArea2(arr2)
  print(f"The maximum volume of water in {arr2}: {result2}")