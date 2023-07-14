class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l=0
        r=int(sqrt(c))
        while l<=r:
            res=(l*l)+(r*r)
            if res==c:
                return True
            else:
                if res>c:
                    r-=1
                else:
                    l+=1
        return False