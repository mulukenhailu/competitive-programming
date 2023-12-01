class Solution:
    def freqAlphabets(self, s: str) -> str:
        mp={}
        for i in range(26):
            mp[i+1]=chr(97+i)

        onel=[]
        ans=""
        i=0
        while i < len(s):
            if i+2<len(s) and s[i+2]=="#":
                onel.append(s[i:i+2])
                i+=3
            else:
                onel.append(s[i])
                i+=1

        
        for num in onel:
            ans+=(mp[int(num)])
            
        return ans
    
        
            
        
        