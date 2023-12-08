class Solution:
    def totalMoney(self, n: int) -> int:
        
        # 0123456
        # 789 10 11 12 13 14
        start=0
        ans=0
        p=1
        if n<=7:
            for i in range(1, n+1):
                ans+=i
        else:
            for i in range(n):
                if i%7==0:
                    start+=1
                    for j in range(start, start+7):
                        if p<=n:
                            ans+=j
                            p+=1
        return ans
                
                    
                    
            
            
                