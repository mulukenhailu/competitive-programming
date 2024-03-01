# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merge(r1, r2):
            if not r1 or not r2:
                return r1 or r2

            else:
                root = TreeNode(r1.val + r2.val)
                root.left = merge(r1.left, r2.left)
                root.right = merge(r1.right, r2.right)

            return root
        return merge(root1, root2)


        

              

        