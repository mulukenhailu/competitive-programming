class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        step=0
        pos=target
        while maxDoubles>0 and pos>=1:
            if pos%2:
                step+=1
                pos-=1
            else:
                step+=1
                pos/=2
                maxDoubles-=1

        return int(step+pos-1)

        