class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        pc = Counter(p)
        sc = Counter()

        ans = []
        l=0
        r=0
        while r<len(s):

            sc[s[r]]+=1
            while r-l+1==len(p):
                if sc==pc: 
                    ans.append(l)
                sc[s[l]]-=1
                l+=1
            r+=1

        return ans

        