class Solution:
    def minimizedStringLength(self, s: str) -> int:
        s_count=Counter(s)
        ans=0
        for v in s_count.values():
            ans+=1
        return ans
                
        # a a a a a a
        # a a a a
        # a a
        # a