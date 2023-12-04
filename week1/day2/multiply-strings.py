class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1=num1[::-1]
        num2=num2[::-1]
        n1=[]
        n2=[]
        print(num1)
        print(num2)
        lnum1=len(num1)
        lnum2=len(num2)
        
        for i in range(lnum1):
            n1.append(int(num1[i])*(10**i))
        print(n1)
        
        for i in range(lnum2):
            n2.append(int(num2[i])*(10**i))
        n2=n2[::-1]
        print(n2)
        
        ans=0
        for d1 in n1:
            for d2 in n2:
                ans+=d1*d2
        return str(ans)
        
            
            
            