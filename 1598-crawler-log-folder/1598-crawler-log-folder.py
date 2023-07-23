class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stk=[]
        for log in(logs):
            if  stk and log=="../":
                stk.pop()
            elif not stk and log=="../":
                pass
            elif log=="./":
                pass
            else:
                stk.append(log)
        return len(stk)
                
        