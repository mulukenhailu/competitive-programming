class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1=[]
        stack2=[]
        for c in s:
            if stack1 and c=="#":
                stack1.pop()
                continue
            else:
                if c=="#":
                    continue
                else:
                    stack1.append(c)
                    
        print(stack1)
        
        for c in t:
            if stack2 and c=="#":
                stack2.pop()
                continue
            else:
                if c=="#":
                    continue
                else:
                    stack2.append(c)
        print(stack2)
        
        return stack1==stack2