# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        newnode=TreeNode(val)
        if not root:
            return newnode
        elif not root.left and val<root.val:
            root.left=newnode
        elif not root.right and val>root.val:
            root.right=newnode
        elif val<root.val:
            self.insertIntoBST(root.left, val)
        else:
            self.insertIntoBST(root.right, val)
        return root
        