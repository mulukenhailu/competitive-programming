class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        output, val=0, 0
        for i, p in enumerate(s):
            if p=="(":
                val+=1
            else:
                val-=1
                if s[i-1]=="(":
                    output+=2**val
        return output
        # stack=[]
        # output, val=0, 0
        # for p in s:
        #     if p=="(":
        #         stack.append(0)
        #     elif p==")":
        #         mul=stack.pop()
        #         if mul==0:
        #             val=1
        #         else:
        #             val=mul*2
        #         if not stack:
        #             output+=val 
        #         else:
        #             stack[-1]=val
        # return output
            