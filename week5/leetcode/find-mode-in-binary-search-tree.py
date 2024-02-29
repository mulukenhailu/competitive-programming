# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dic=defaultdict()

        def trav(root):
            if not root:
                return 

            dic[root.val]=dic.get(root.val, 0)+1
            trav(root.left)
            trav(root.right)

        trav(root)
        maxV=max(dic.values())
        ans=[]
        for k, v in dic.items():
            if v==maxV:
                ans.append(k)

        return ans


        