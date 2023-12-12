class Solution:
    def reverseWords(self, s: str) -> str:
        wl=s.lstrip()
        wl=wl.rstrip()
        pos=[]
        for  i in range(len(wl)-1):
            if wl[i]==" " and wl[i+1]==" ":
                continue
            else:
                pos.append(wl[i])   
        ans=""
        for p in pos:
            ans+=p
        ans+=wl[-1]
        
        wl2=ans.split(" ")
        wl2.reverse()
        print(" ".join(wl2))
        
        return " ".join(wl2)
        
            
                
                
                
        # wl=s.split(" ")
        # wl.reverse()
        # ans=" ".join(wl)