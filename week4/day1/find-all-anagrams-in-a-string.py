class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pc=Counter(p)
        n=len(s)
        ans=[]
        for i in range(n-len(p)+1):
            if Counter(s[i:i+len(p)]) == pc:
                ans.append(i)
        return ans
        