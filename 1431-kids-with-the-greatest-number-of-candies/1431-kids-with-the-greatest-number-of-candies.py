class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        _maxCandy=max(candies)
        ans=[]
        for c in candies:
            if c+extraCandies>=_maxCandy:
                ans.append(True)
            else:
                ans.append(False)
        print(ans)
        return ans
            
        