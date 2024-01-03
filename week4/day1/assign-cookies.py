class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        gg=0
        ss=0
        ans=0
        while gg<len(g) and ss<len(s):
            if g[gg]>s[ss]:
                gg+=1
            elif g[gg]<=s[ss]:
                gg+=1
                ss+=1
                ans+=1
        return ans
        