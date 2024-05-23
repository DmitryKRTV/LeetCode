# https://leetcode.com/problems/invert-binary-tree/description/

# Given the root of a binary tree, invert the tree, and return its root.

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            stack = deque()
            stack.append(root)
            while stack:
                node = stack.popleft()
                node.left, node.right = node.right, node.left   
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)   
        return root