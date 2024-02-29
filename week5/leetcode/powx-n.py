class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x, n):
            if n == 0:
                return 1
            if x == 0:
                return float(0)
            if n % 2 == 0:
                return pow(x * x, n // 2)
            if n > 0:
                return x * pow(x, n - 1)
            else:
                return 1 / pow(x, -n)

        return pow(x, n)


            

        