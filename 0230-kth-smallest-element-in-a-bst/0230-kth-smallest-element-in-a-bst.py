from heapq import heappush, heapreplace

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        
        def inorder(root):
            if not root:
                return 
            
            inorder(root.left)
            
            if len(heap) != k:  
                heappush(heap, -root.val)
            else:
                if root.val < -heap[0]:
                    heapreplace(heap, -root.val)
                
            inorder(root.right)
            
        inorder(root)
        return -heap[0]  
