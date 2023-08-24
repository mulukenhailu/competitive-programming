# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def inorder(root1, root2):
            if not root1:
                return
            inorder(root1.left, root2.left)
            if root1 is target:
                self.ans=root2
            inorder(root1.right, root2.right)
        inorder(original, cloned)
        return self.ans
        