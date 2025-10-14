"""
Given an array nums of n integers and an integer k, determine whether there exist two adjacent subarrays of length k such that both subarrays are strictly increasing. Specifically, check if there are two subarrays starting at indices a and b (a < b), where:

Both subarrays nums[a..a + k - 1] and nums[b..b + k - 1] are strictly increasing.
The subarrays must be adjacent, meaning b = a + k.
Return true if it is possible to find two such subarrays, and false otherwise.

 

Example 1:

Input: nums = [2,5,7,8,9,2,3,4,3,1], k = 3

Output: true

Explanation:

The subarray starting at index 2 is [7, 8, 9], which is strictly increasing.
The subarray starting at index 5 is [2, 3, 4], which is also strictly increasing.
These two subarrays are adjacent, so the result is true.
Example 2:

Input: nums = [1,2,3,4,4,4,4,5,6,7], k = 5

Output: false

 

Constraints:

2 <= nums.length <= 100
1 < 2 * k <= nums.length
-1000 <= nums[i] <= 1000
"""
from typing import List

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        
        def is_increasing(l, r):
            for i in range(l + 1, r):
                if nums[i] <= nums[i - 1]:
                    return False
            return True
    
        for a in range(n - 2 * k + 1):
            if is_increasing(a, a + k) and is_increasing(a + k, a + 2 * k):
                return True
        return False
        

nums =[-3,-19,-8,-16]
k = 2
solution=Solution()
print(solution.hasIncreasingSubarrays(nums,k))

"""
[2,5,7,8,9,2,3,4,3,1]
3
[0,4,16,20,-6]
2
[5,8,-2,-1]
2
[-15,-13,4,7]
2
[-15,19]
1
[6,13,-17,-20,2]
2
[5,8,-2,-1]
2
[0,-10,9,12,-19,-18,20]
2
"""