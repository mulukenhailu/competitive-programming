# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dc(left, right):
            if left==right:
                return None
            # if len(arr)==1:
            #     return TreeNode(arr[0])

            mid=(left + right)//2
            cur=TreeNode(nums[mid])

            left=dc(left, mid)
            right=dc(mid+1, right)

            cur.left=left
            cur.right=right
            return cur

        return dc(0, len(nums))



        