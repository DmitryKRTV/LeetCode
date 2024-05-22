# https://leetcode.com/problems/root-equals-sum-of-children/description/

# You are given the root of a binary tree that consists of exactly 3 nodes: the root, its left child, and its right child.
# Return true if the value of the root is equal to the sum of the values of its two children, or false otherwise.
# Example 1:

# Input: root = [10,4,6]
# Output: true
# Explanation: The values of the root, its left child, and its right child are 10, 4, and 6, respectively.
# 10 is equal to 4 + 6, so we return true.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def checkTree(self, root: TreeNode) -> bool:
        return root.val == root.left.val + root.right.val
    
root = TreeNode(10)
root.left = TreeNode(4)
root.right = TreeNode(5)
sol = Solution()
print(sol.checkTree(root))