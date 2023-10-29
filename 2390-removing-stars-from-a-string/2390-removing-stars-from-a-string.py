class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        for c in s:
            if stack and c=="*":
                stack.pop()
            else:
                stack.append(c)
        ans=""
        for c in stack:
            ans+=c
        return ans
        
        
        
        # stk=[]
        # for char in s:
        #     if char == "*":
        #         stk.pop()
        #     else:
        #         stk.append(char)
        # ans=""
        # for c in stk:
        #     ans=ans+c
        # return ans
            
        