# Hand of Straights
# https://leetcode.com/problems/hand-of-straights/description/
# Leetcode: 846

# Same question: Divide Array in Sets of K Consecutive Numbers
# https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/description/
# Leetcode: 1296

'''
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

 

Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
Example 2:

Input: hand = [1,2,3,4,5], groupSize = 4
Output: false
Explanation: Alice's hand can not be rearranged into groups of 4.

 

Constraints:

1 <= hand.length <= 104
0 <= hand[i] <= 109
1 <= groupSize <= hand.length
'''
from typing import List
import heapq
from collections import Counter

class Solution:
  # Time Complexity: O(n log n)
  # Space Complexity: O(n)  
  def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
    if len(hand) % groupSize:
      return False
    
    count = Counter(hand)
    minHeap = list(count.keys())
    heapq.heapify(minHeap)

    while minHeap:
      first = minHeap[0]

      for card in range(first, first + groupSize):
        if card not in count:
          return False
        
        count[card] -= 1
        if count[card] == 0:
          if card != minHeap[0]:
            return False
          heapq.heappop(minHeap)

    return True
  
if __name__ == "__main__":
  solution = Solution()

  hand = [1,2,3,6,2,3,4,7,8]
  groupSize = 3
  result = solution.isNStraightHand(hand, groupSize)
  print(f"Can the hand {hand} be rearranged into groups of size {groupSize}? {result}")

  hand = [1,2,3,4,5]
  groupSize = 4
  result = solution.isNStraightHand(hand, groupSize)
  print(f"Can the hand {hand} be rearranged into groups of size {groupSize}? {result}")
        