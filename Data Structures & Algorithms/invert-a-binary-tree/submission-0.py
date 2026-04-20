# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def search_and_reverse(root):
            if not root:
                return 
            tmp = root.right
            root.right = root.left
            root.left = tmp
            search_and_reverse(root.right)
            search_and_reverse(root.left)
        search_and_reverse(root)
        return root