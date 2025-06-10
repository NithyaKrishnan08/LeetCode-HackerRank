# Next Greater Element I

'''
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

 

Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
Example 2:

Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
 

Constraints:

1 <= nums1.length <= nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 104
All integers in nums1 and nums2 are unique.
All the integers of nums1 also appear in nums2.
'''
from typing import List

class Solution:
  # Brute force solution
  def nextGreaterElement1(self, nums1: List[int], nums2: List[int]) -> List[int]:
    n = len(nums1)
    m = len(nums2)
    ans = []

    for i in range(n):
      each_num = nums1[i]
      found = False

      for j in range(m):       
        if nums2[j] == each_num:
          for k in range(j + 1, m):
            if nums2[k] > each_num:
              ans.append(nums2[k])
              found = True
              break
          break

      if not found:
        ans.append(-1)

    return ans
  
  # Optimal solution
  def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    next_greater_map = {}
    stack = []

    for num in nums2:
      while stack and stack[-1] < num:
        next_greater_map[stack.pop()] = num
      stack.append(num)

    while stack:
      next_greater_map[stack.pop()] = -1

    return [next_greater_map[k] for k in nums1]

  
if __name__ == "__main__":
  nums1 = [4,1,2]
  nums2 = [1,3,4,2]
  solution = Solution()
  result = solution.nextGreaterElement(nums1, nums2)
  print(result)