# Candy

'''
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

 

Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
 

Constraints:

n == ratings.length
1 <= n <= 2 * 104
0 <= ratings[i] <= 2 * 104
'''
from typing import List

class Solution:
  # Brute force solution
  # TC: O(3N)
  # SC: O(2N)
  def candy1(self, ratings: List[int]) -> int:
    n = len(ratings)
    left_neighbors = [0] * n
    right_neighbors = [0] * n

    left_neighbors[0] = 1
    right_neighbors[n - 1] = 1

    # Filling in left_neighbors array
    for i in range(1, n):
      if ratings[i] > ratings[i - 1]:
        left_neighbors[i] = left_neighbors[i - 1] + 1
      else:
        left_neighbors[i] = 1

    # Filling in right_neighbors array
    for i in range(n - 2, -1, -1):
      if ratings[i] > ratings[i + 1]:
        right_neighbors[i] = right_neighbors[i + 1] + 1
      else:
        right_neighbors[i] = 1

    max_candies = 0
    for i in range(n):
      max_candies = max_candies + max(left_neighbors[i], right_neighbors[i])

    return max_candies
  
  # Optimal solution
  # TC: O(N)
  # SC: O(1)
  def candy(self, ratings: List[int]) -> int:
    n = len(ratings)
    max_candies = 1
    i = 1

    while i < n:
      # For flat elements
      if ratings[i] == ratings[i - 1]:
        max_candies += 1
        i += 1
        continue

      # Travelling from bottom to peak
      peak = 1
      while i < n and ratings[i] > ratings[i - 1]:
        peak += 1
        max_candies += peak
        i += 1

      # Travelling from peak to bottom
      down = 1
      while i < n and ratings[i] < ratings[i - 1]:
        max_candies += down
        i += 1
        down += 1

      if down > peak:
        max_candies += (down - peak)
      
    return max_candies
  
if __name__ == "__main__":
  solution = Solution()
  ratings = [1,0,2]
  result = solution.candy(ratings)
  print(result)