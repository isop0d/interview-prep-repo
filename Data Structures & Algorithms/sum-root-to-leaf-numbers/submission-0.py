# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
in order traversal,

helper function for the addition to sum

sum variable
 
   4
  9   0
5  1

keep path and root

helper to add curr root val to the sum

recursive call to left 
recursive call to the right 

'''
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        sum = 0

        def dfs(root: Optional[TreeNode], path: str = ''):

            nonlocal sum

            if not root:
                return -1

            path += str(root.val)

            if (not root.left and not root.right):
                sum += int(path)

            dfs(root.left, path)
            dfs(root.right, path)

        dfs(root)
        return sum