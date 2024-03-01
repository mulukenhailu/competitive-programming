# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.ans=float("-inf")

        def maxDiff(root, minV, maxV):
            if not root:
                self.ans=max(self.ans, abs(maxV-minV))
                return 

            minV=min(root.val, minV)
            maxV=max(root.val, maxV)
            maxDiff(root.left, minV, maxV)
            maxDiff(root.right, minV, maxV)

        maxDiff(root, float("inf"), float("-inf"))
        return self.ans



        