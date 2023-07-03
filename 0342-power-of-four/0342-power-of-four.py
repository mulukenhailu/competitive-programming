class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1:
            return True
        for i in range(n//2):
            res=(4**i)
            if n==res:
                return True
            elif res>n:
                return False
     