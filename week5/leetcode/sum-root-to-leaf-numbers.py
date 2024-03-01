# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def cal(root, val):
            if not root:
                return val

            val=root.val+10*val
            ans=0
            if root.left: ans+=cal(root.left, val)
            if root.right: ans+=cal(root.right, val)

            return ans or val

        return cal(root, 0)
            

        