"""
Given the root of a binary tree and an integer targetSum, 
return all root-to-leaf paths where the sum of the node values in the path equals targetSum. 
Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

Example 1:

https://assets.leetcode.com/uploads/2021/01/18/pathsumii1.jpg

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22


Example 2:
https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg

Input: root = [1,2,3], targetSum = 5
Output: []
Example 3:

Input: root = [1,2], targetSum = 0
Output: []
 

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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root==None:
            return []
        if root.left is None and root.right is None:
            if targetSum == root.val:
                return [[root.val]]
            else:
                return []

        left=self.pathSum(root.left, targetSum - root.val)
        if(left!=[]):
            for list in left:
                list.insert(0, root.val)

        right=self.pathSum(root.right, targetSum - root.val)
        if(right!=[]):
            for list in right:
                list.insert(0, root.val)
        
        return left+right

node1=TreeNode(7)
node2=TreeNode(2)
node3=TreeNode(13)
node4=TreeNode(1)
node9=TreeNode(5)

node5=TreeNode(11,node1,node2)
node6=TreeNode(4,node5,None)

node7=TreeNode(4,node9,node4)
node8=TreeNode(8,node3,node7)
root=TreeNode(5,node6,node8)

solution = Solution()
print(solution.pathSum(root,22))

