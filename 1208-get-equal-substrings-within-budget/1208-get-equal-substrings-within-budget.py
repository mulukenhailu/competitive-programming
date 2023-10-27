class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l=r=cost=ans=0
        while r<len(s):
            cost+=abs(ord(s[r])-ord(t[r]))
            while cost>maxCost:
                cost-=abs(ord(s[l])-ord(t[l]))
                l+=1
            ans=max(ans, r-l+1)
            r+=1
        return ans