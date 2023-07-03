class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==1 or n==3:
            return True
        for i in range(n//2):
            res=(3**i)
            if n==res:
                return True
            elif res>n:
                return False
        