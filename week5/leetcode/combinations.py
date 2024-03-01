class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]

        def bt(first_num, comb):
            if len(comb)==k:
                ans.append(comb[:])
                return 

            for next_num in range(first_num, n+1):
                comb.append(next_num)
                bt(next_num+1, comb)
                comb.pop()

            return ans

        return bt(1, [])






