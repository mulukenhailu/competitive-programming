# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans=0
        queue = deque([(root, 0)])
        
        while queue:
            node, firstNum= queue[0]
            n = len(queue)
            for i in range(n):
                node, index = queue.popleft()
                
                if node.left:
                    queue.append((node.left, 2*index))
                
                if node.right:
                    queue.append((node.right, 2*index+1))
                    
            ans = max(ans, index - firstNum + 1)
            
        return ans
        