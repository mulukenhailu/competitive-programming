class Solution:
    def removeStars(self, s: str) -> str:
        stk=[]
        for char in s:
            if char == "*":
                stk.pop()
            else:
                stk.append(char)
        ans=""
        for c in stk:
            ans=ans+c
        return ans
            
        