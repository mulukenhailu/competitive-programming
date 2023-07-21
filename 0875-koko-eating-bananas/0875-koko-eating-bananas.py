class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        
        l=1
        r=max(piles) 
        
        while l<=r:
            mid=l+(r-l)//2
            if self.printer(piles, mid)<=h: 
                r=mid-1 
            else:
                l=mid+1
        return l 

    def printer(self, piles, mid):
        time=0
        for pile in piles:
            time+=math.ceil(pile/mid)
        return time

            



        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         poss_k=[i for i in range(min(piles), max(piles)+1)]
#         for i in poss_k:
#             time=0
#             for pile in piles:
#                 if i==pile or pile%i==0:
#                     time+=(pile)/i
#                 else:
#                     time+=((pile)//i)+1
#         return int(time)
    
    
    
    
    
    
    
    #     if len(piles)==h:
    #         return max(piles)
    #     poss_k=[i for i in range(min(piles), max(piles)+1)]
    #     low=0
    #     high=len(poss_k)-1
    #     while low<= high:
    #         mid=(low+high)//2
    #         time=0
    #         for pile in piles:
    #             if poss_k[mid]==pile:
    #                 time+=(pile)/poss_k[mid]
    #             else:
    #                 time+=(pile)//poss_k[mid]+1
    #         if time==h:
    #             return poss_k[mid]
    #         elif time<h:
    #             high=mid-1
    #         elif time>h:
    #             low=mid-1
        
        