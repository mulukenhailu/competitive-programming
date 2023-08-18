class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
#         459       
#         455....455
#         453....345
#         =12
        
        
#         4367.....3467....3464....k=2    
#         3464......3446....3444...k=1
#         3443......3444....3442...k=0
#         =12
        
        # for _ in range(k):
        #     piles.sort()
        #     l=piles.pop()
        #     if l%2==0:
        #         ans=l/2
        #     else:
        #         ans=floor(l/2)+1
        #     piles.append(ans)
        # return int(sum(piles))
        
        for i, p in enumerate(piles):
            piles[i]=-p
        heapify(piles)
        for _ in range(k):
            l=-heappop(piles)
            if l%2==0:
                ans=l/2
            else:
                ans=floor(l/2)+1
            heappush(piles, -ans)
        return int(-sum(piles))
            
            
            
            
        