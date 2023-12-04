class Solution:
    def printVertically(self, s: str) -> List[str]:
        lst=s.split(" ")
        maxl=0
        ans=[]
        for w in lst:
            maxl=max(len(w), maxl)
        temp=""
        for i in range(maxl):
            for w in lst:
                if i<(len(w)):
                    temp+=w[i]
                else:
                    temp+=" "
            print(temp)
            ans.append(temp.rstrip())
            temp=""
            
        return (w for w in ans)
                
            
            
            
            
        
        