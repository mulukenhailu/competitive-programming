# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # if not root.left and not root.right:
        #     return True
        # if root.left.val >= root.val or root.right.val < root.val:
        #     return False
        # left=self.isValidBST(root.left)
        # right=self.isValidBST(root.right)
        # return left and right
        def check(root, left, right):
            if not root:
                return True
            if left >= root.val or right <= root.val:
                return False
            l=check(root.left, left, root.val)
            r=check(root.right, root.val, right)
            return l and r
        return check(root, -float("inf"), float("inf"))
        
        