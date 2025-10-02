"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Example 1:

https://assets.leetcode.com/uploads/2021/01/18/pathsum1.jpg

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.


Example 2:
https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg

Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There are two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.
Example 3:

Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000

"""

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

from typing import List,Optional

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None:
            return targetSum == root.val
        return (
            self.hasPathSum(root.left, targetSum - root.val) or
            self.hasPathSum(root.right, targetSum - root.val)
        )

node1=TreeNode(7)
node2=TreeNode(2)
node3=TreeNode(13)
node4=TreeNode(1)

node5=TreeNode(11,node1,node2)
node6=TreeNode(4,None,node4)

node7=TreeNode(4,node5,None)
node8=TreeNode(8,node3,node6)
root=TreeNode(5,node6,node8)

solution = Solution()
print(solution.hasPathSum(root,22))

