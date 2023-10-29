class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack=[]
        for op in logs:
            if stack and op=="../":
                stack.pop()
            else:
                if op != "./" and op != "../":
                    stack.append(op)
        return len(stack)
        
        
        
        
        
        
        
        
        # stk=[]
        # for log in(logs):
        #     if  stk and log=="../":
        #         stk.pop()
        #     elif not stk and log=="../":
        #         pass
        #     elif log=="./":
        #         pass
        #     else:
        #         stk.append(log)
        # return len(stk)
                
        