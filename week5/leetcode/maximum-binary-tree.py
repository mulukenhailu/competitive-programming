# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def maxTree(lst):

            maxV=max(lst)
            maxidx=lst.index(maxV)

            root=TreeNode(maxV)

            prefix=lst[:maxidx]
            suffix=lst[maxidx+1:]

            if prefix:root.left=maxTree(prefix)
            if suffix:root.right=maxTree(suffix)

            return root

        return maxTree(nums)



        