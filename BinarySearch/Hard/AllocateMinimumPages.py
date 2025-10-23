# Allocate Minimum Pages

'''
Given an array arr[], where arr[i] represents the number of pages in the i-th book, and an integer k denoting the total number of students, allocate all books to the students such that:

Each student gets at least one book.
Books are allocated in a contiguous sequence.
The maximum number of pages assigned to any student is minimized.
If it is not possible to allocate all books among k students under these conditions, return -1.

Examples:

Input: arr[] = [12, 34, 67, 90], k = 2
Output: 113
Explanation: Books can be distributed in following ways:

[12] and [34, 67, 90] - The maximum pages assigned to a student is  34 + 67 + 90 = 191.
[12, 34] and [67, 90] - The maximum pages assigned to a student is 67 + 90 = 157.
[12, 34, 67] and [90] - The maximum pages assigned to a student is 12 + 34 + 67 = 113.
The third combination has the minimum pages assigned to a student which is 113.

Input: arr[] = [15, 17, 20], k = 5
Output: -1
Explanation: Since there are more students than total books, it's impossible to allocate a book to each student.

Input: arr[] = [22, 23, 67], k = 1
Output: 112
Explanation: Since there is only 1 student, all books are assigned to that student. So, maximum pages assigned to a student is 22 + 23 + 67 = 112.
'''
from typing import List

class Solution:
  def allocateMinimumPages(self, arr: List[int], k: int) -> int:
    n = len(arr)
    if n < k:
      return -1
    
    if k == 1:
      return sum(arr)
    
    def calculateStudents(pages):
      no_of_students, pages_per_student = 1, 0

      for num in arr:
        if pages_per_student + num <= pages:
          pages_per_student += num
        else:
          no_of_students += 1
          pages_per_student = num

      return no_of_students

    low, high = max(arr), sum(arr)
    answer = -1

    while low <= high:
      mid = (low + high) // 2

      if calculateStudents(mid) <= k:
        answer = mid
        high = mid - 1
      else:
        low = mid + 1

    return answer
  
if __name__ == '__main__':
  sol = Solution()
  print(sol.allocateMinimumPages(arr = [12, 34, 67, 90], k = 2)) # 113
  print(sol.allocateMinimumPages(arr = [15, 17, 20], k = 5)) # -1
  print(sol.allocateMinimumPages(arr = [22, 23, 67], k = 1)) # 112