'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
'''

# Brute Force Solution 
# Time Complexity - O(N^3 * log(no. of unique triplets))
# Space Complexity - O(2 * no. of the unique triplets)
def threeSum1(nums):
  n = len(nums)
  tripletsArray = set()

  for i in range(n):
    for j in range(i + 1, n):
      for k in range(j + 1, n):
        if nums[i] + nums[j] + nums[k] == 0:
          temp = [nums[i], nums[j], nums[k]]
          temp.sort()
          tripletsArray.add(tuple(temp))
  
  result = list(tripletsArray)
  return result

# Better Solution - Hashmap
# Time Complexity - O(N^2 * log(no. of unique triplets))
# Space Complexity - O(2 * no. of the unique triplets)

def threeSum2(nums):
  n = len(nums)
  tripletsArray = set()

  for i in range(n):
    hashSet = set()
    for j in range(i + 1, n):
      third = -(nums[i] + nums[j])
      if third in hashSet:
        temp = [nums[i], nums[j], third]
        temp.sort()
        tripletsArray.add(tuple(temp))
      hashSet.add(nums[j])     
  
  result = list(tripletsArray)
  return result

# Optimized Solution - O(N)
# Time Complexity - O(N^2) + O(N log N)
# Space Complexity - O(No. of triplets)

def threeSum3(nums):
  n = len(nums)
  sortedNums = sorted(nums)
  tripletsArray = set()

  for i in range(n):
    if(i > 0 and sortedNums[i] ==  sortedNums[i-1]):
      continue

    j = i + 1
    k = n - 1

    while(j < k):
      sum = sortedNums[i] + sortedNums[j] + sortedNums[k]
      if sum < 0:
        j += 1
      elif sum > 0:
        k -= 1
      else:
        temp = [sortedNums[i], sortedNums[j], sortedNums[k]]
        tripletsArray.add(tuple(temp))
        j += 1
        k -= 1
        while (j < k and sortedNums[j] ==  sortedNums[j - 1]):
          j += 1
        while (j < k and sortedNums[k] == sortedNums[k + 1]):
          k -= 1
  
  result = list(tripletsArray)
  return result

if __name__ == "__main__":
  arr1 = [-1,0,1,2,-1,-4]
  arr2 = [0,1,1]
  arr3 = [0,0,0]
  
  print("Brute force solution:")
  result1 = threeSum1(arr1)
  print(f"The triplets of {arr1}: {result1}")

  result2 = threeSum1(arr2)
  print(f"The triplets of {arr2}: {result2}")

  result3 = threeSum1(arr3)
  print(f"The triplets of {arr3}: {result3}")

  print("Better solution:")
  result4 = threeSum2(arr1)
  print(f"The triplets of {arr1}: {result4}")

  result5 = threeSum2(arr2)
  print(f"The triplets of {arr2}: {result5}")

  result6 = threeSum2(arr3)
  print(f"The triplets of {arr3}: {result6}")

  print("Optimal solution:")
  result7 = threeSum3(arr1)
  print(f"The triplets of {arr1}: {result7}")

  result8 = threeSum3(arr2)
  print(f"The triplets of {arr2}: {result8}")

  result9 = threeSum3(arr3)
  print(f"The triplets of {arr3}: {result9}")
