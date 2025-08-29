# Maximum Units on a Truck
# https://leetcode.com/problems/maximum-units-on-a-truck/description/?envType=problem-list-v2&envId=7p5x763&sorting=W3sic29ydE9yZGVyIjoiREVTQ0VORElORyIsIm9yZGVyQnkiOiJGUkVRVUVOQ1kifV0%3D&page=1
# Leetcode Problem 1710: Maximum Units on a Truck

'''
You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

numberOfBoxesi is the number of boxes of type i.
numberOfUnitsPerBoxi is the number of units in each box of the type i.
You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

Return the maximum total number of units that can be put on the truck.

 

Example 1:

Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Output: 8
Explanation: There are:
- 1 box of the first type that contains 3 units.
- 2 boxes of the second type that contain 2 units each.
- 3 boxes of the third type that contain 1 unit each.
You can take all the boxes of the first and second types, and one box of the third type.
The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.
Example 2:

Input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
Output: 91
 

Constraints:

1 <= boxTypes.length <= 1000
1 <= numberOfBoxesi, numberOfUnitsPerBoxi <= 1000
1 <= truckSize <= 106
'''
from typing import List

class Solution:
  def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
    boxTypes.sort(key = lambda x: x[1], reverse=True)

    total_units = 0
    for num_boxes, units_per_box in boxTypes:
      if truckSize == 0:
        break
        
      boxes_to_take = min(num_boxes, truckSize)
      total_units += boxes_to_take * units_per_box
      truckSize -= boxes_to_take

    return total_units

if __name__ == "__main__":
  s = Solution()
  print(s.maximumUnits([[1,3],[2,2],[3,1]], 4))  # 8
  print(s.maximumUnits([[5,10],[2,5],[4,7],[3,9]], 10))  # 91  