# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(p, q):
            if (not p and q) or (p and not q): 
                return False
            if not p and not q : 
                return True

            left=check(p.left, q.left)
            right=check(p.right, q.right)

            return left and right and p.val == q.val

        return check(p, q)

            

        