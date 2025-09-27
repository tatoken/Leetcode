"""
Given an array of points on the X-Y plane points where points[i] = [xi, yi],
return the area of the largest triangle that can be formed by any three different points.
Answers within 10-5 of the actual answer will be accepted.

 

Example 1:
https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/04/1027.png

Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2.00000
Explanation: The five points are shown in the above figure. The red triangle is the largest.
Example 2:

Input: points = [[1,0],[0,0],[0,1]]
Output: 0.50000

Constraints:

3 <= points.length <= 50
-50 <= xi, yi <= 50
All the given points are unique.
"""

from typing import List
from scipy.spatial import ConvexHull
from itertools import combinations

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        points = [tuple(p) for p in points]
        hull = ConvexHull(points)
        hull_points = [points[i] for i in hull.vertices]
        
        def area(p1, p2, p3):
            return abs(
                p1[0]*(p2[1]-p3[1]) +
                p2[0]*(p3[1]-p1[1]) +
                p3[0]*(p1[1]-p2[1])
            ) / 2.0
        
        max_area = 0
        for a, b, c in combinations(hull_points, 3):
            max_area = max(max_area, area(a, b, c))
        return max_area
                
      
points=[[1,0],[0,0],[0,1]]
solution=Solution()
print(solution.largestTriangleArea(points))