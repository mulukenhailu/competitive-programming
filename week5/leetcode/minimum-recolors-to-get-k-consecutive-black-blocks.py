class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        wc=0
        l=0
        ans=float("inf")
        for r in range(len(blocks)):
            if blocks[r]=="W":
                wc+=1
            while r-l+1==k:
                ans=min(ans, wc)
                if blocks[l]=="W":
                    wc-=1
                l+=1

        print(ans)
        return ans

        