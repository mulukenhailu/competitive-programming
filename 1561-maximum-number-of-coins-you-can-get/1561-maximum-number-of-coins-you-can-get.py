class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        high=len(piles)-2
        low=0
        res=0
        while(low<=high):
            res+=piles[high]
            low+=1
            high-=2
        return res
        