class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set() 
        while n != 1: 
            sum_= 0
            while n > 0:
                s = n % 10
                sum_ += s ** 2
                n //= 10
            if sum_ in seen:
                return False
            n = sum_
            seen.add(sum_)
        return True