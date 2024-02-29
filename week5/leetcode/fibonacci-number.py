class Solution:
    def fib(self, n: int) -> int:
        first=0
        second=1


        if n==0:
            return 0

        for i in range(2, n+1):
            temp=first
            first=second
            second=temp+second

        return second
        