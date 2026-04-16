# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=-2, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.best = 0

        def dfs(node):
            if not node:
                return 0
            
            leftdfs = dfs(node.left)
            rightdfs = dfs(node.right)

            self.best = max(self.best, (leftdfs + rightdfs))

            return max(leftdfs, rightdfs) + 1
        dfs(root)
        return self.best