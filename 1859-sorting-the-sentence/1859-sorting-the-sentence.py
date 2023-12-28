class Solution:
    def sortSentence(self, s: str) -> str:
        wlist=s.split(" ")
        wlist.sort(key=lambda x : x[-1])
        ans=[]
        for w in wlist:
            ans.append(w[:-1])
            
        return " ".join(ans)