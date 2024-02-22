class Solution:
    def longestPalindrome(self, s: str) -> int:
        c=Counter(s)

        print(c)
        flag=False

        if len(c.keys())==1:
            return len(s)

        ans=0
        for k, v in c.items():
            if not v%2:
                ans+=v
            elif v>1 and v%2:
                ans+=v-1
                flag=True

        if flag or (1 in c.values()):
            ans+=1

        return ans

        