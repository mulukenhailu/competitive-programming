class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans=""
        for i, v in enumerate(spaces):
            if i==0:
                ans=ans+s[:v]+" "
            else:
                ans=ans+s[spaces[i-1]:v]+" "
        return ans+s[spaces[-1]:]
        