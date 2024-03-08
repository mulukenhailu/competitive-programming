class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]

        def bt(cur, opening, closing):
            if closing > opening or opening > n:
                return
            if len(cur)==2*n :
                ans.append("".join(cur))
                return 

            cur.append("(")
            bt(cur, opening+1, closing)
            cur.pop()

            cur.append(")")
            bt(cur, opening, closing+1)
            cur.pop()


        bt([], 0, 0)
        return ans

