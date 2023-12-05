class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans=[]
        for i in range(len(num)-2):
            if len(set(num[i:i+3]))==1:
                ans.append(num[i:i+3])
        print(ans)
        
        if ans:
            _max=max(ans)
            if _max==0:
                return "000"
            else:
                return str(max(ans))
        else:
            return ""
                
        
        
        
            