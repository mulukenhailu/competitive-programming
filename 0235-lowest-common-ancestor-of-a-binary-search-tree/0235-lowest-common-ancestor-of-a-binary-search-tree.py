# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def check(root, p, q):
            if p.val > root.val and q.val < root.val or p.val < root.val and q.val > root.val:
                return root
            if root.val == p.val:
                return p
            if root.val == q.val:
                return q
            if p.val < root.val and q.val < root.val:
                return check(root.left, p, q)
            if p.val > root.val and q.val > root.val:
                return check(root.right, p, q)

        return check(root, p, q)
        