# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def ances(root, p, q):
            if root.val == p.val or root.val == q.val:
                return root
            if (p.val < root.val and q.val > root.val) or (p.val > root.val and q.val < root.val):
                return root

            if p.val < root.val and q.val < root.val:
                return ances(root.left,p, q)
            
            if p.val > root.val and q.val > root.val:
                return ances(root.right, p, q)

        return ances(root, p, q)


        