class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        l=len(strs)
        ans=0
        for c in range(len(strs[0])):
            for r in range(l-1):
                print(r, c, "...", r+1, c)
                if ord(strs[r][c]) > ord(strs[r+1][c]):
                    ans+=1
                    break
                    
        print(ans)
        return ans
                    
        