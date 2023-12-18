class Solution:
    def romanToInt(self, s: str) -> int:
        numerals=["I", "V", "X", "L", "C", "D" , "M"]
        values=[1, 5, 10, 50, 100, 500, 1000]
        pair={n:v  for n, v in zip(numerals, values)}
        ans=0
        i=0
        while i < len(s):
            if s[i]=="V" or s[i]=="L" or s[i]=="D" or s[i]=="M" :
                ans+=pair[s[i]]
                i+=1
            elif i+1<len(s) and  s[i]=="I" and s[i+1]=="V":
                ans+=4
                i+=2
            elif i+1<len(s) and s[i]=="I" and s[i+1]=="X":
                ans+=9
                i+=2
            elif i+1<len(s) and s[i]=="X" and s[i+1]=="L":
                ans+=40
                i+=2
            elif i+1<len(s) and s[i]=="X" and s[i+1]=="C":
                ans+=90
                i+=2
            elif i+1<len(s) and s[i]=="C" and s[i+1]=="D":
                ans+=400
                i+=2
            elif i+1<len(s) and s[i]=="C" and s[i+1]=="M":
                ans+=900
                i+=2
            else:
                ans+=pair[s[i]]
                i+=1
        print(ans)
        return ans
            
                
                
        