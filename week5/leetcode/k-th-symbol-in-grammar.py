class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0

        parent = self.kthGrammar(n - 1, (k + 1) // 2)

        if parent == 0:
            return 0 if k % 2 == 1 else 1
        else:
            return 1 if k % 2 == 1 else 0


        # 1=0
        # 2=01
        # 3=01 10
        # 4=01 10 10 01
        # 5=01 10 10 01 10 01 01 10
        # 6=01 10 10 01 10 01 01 10 10 01 01 10 01 10 10 01

        