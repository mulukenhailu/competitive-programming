class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[["."]*n for _ in range(n)]
        ans=[]

        col=set()
        pos=set()
        neg=set()

        def bt(r):
            if r >= n:
                temp=["".join(row) for row in board]
                ans.append(temp)
                return 

            for c in range(n):
                if (c in col) or (r + c in  pos) or (r-c in neg):
                    continue
                    
                col.add(c)
                pos.add(r+c)
                neg.add(r-c)
                board[r][c]="Q"

                bt(r+1)

                col.remove(c)
                pos.remove(r+c)
                neg.remove(r-c)
                board[r][c]="."

        bt(0)
        return ans



        