class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n=len(s)
        ans=""
        flag=True

        if n<2:
            return ""

        for st in range(n):
            for ed in range(st + 1, n+1):
                cur=s[st:ed]
                for c in cur:
                    if  c.swapcase() in s[st:ed]:pass
                    else:flag=False
                if flag: ans=max(ans, s[st:ed], key=len)
                flag=True
        return ans
                


        