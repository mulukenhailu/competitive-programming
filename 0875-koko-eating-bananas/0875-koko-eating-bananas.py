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
        return time             #timme O(logn)  space O(1)

    # l=1, r=11....true
    # m=6 p=1+1+2+2=6<h=8 
    # l=1, r=5......true
    # m=3 p=1+2+3+4=10>h=8
    # l=4, r=5......true
    # m=4, p=1+2+2+3=h=8
    # l=4, r=4.......true
    # m=4, p=1+2+2+3=h=8
    # l=4, r=3.....False
    # return >>>>l=4         
    
            



        
        
        
        
        
        
        
 
        