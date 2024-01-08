class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s2c=Counter(s1)
        s1c=Counter()

        l=0
        r=0

        while r<len(s2):
            s1c[s2[r]]+=1
            while r-l+1==len(s1):
                if s1c==s2c:
                    return True
                s1c[s2[l]]-=1
                l+=1    
            r+=1
        return False
        