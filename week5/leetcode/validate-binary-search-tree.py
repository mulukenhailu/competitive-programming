# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validity(root, left, right):
            if not root:
                return True
            if left >= root.val or right <= root.val:
                return False

            left=validity(root.left, left, root.val)
            right=validity(root.right, root.val , right)

            return left and right  

        return validity(root, -float("inf"), float("inf"))

            
