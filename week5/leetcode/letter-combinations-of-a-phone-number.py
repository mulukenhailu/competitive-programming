class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "": return []
        mapping={
            "2":'abc',
            "3":'def',
            "4":'ghi',
            "5":'jkl',
            "6":'mno',
            "7":'pqrs',
            "8":'tuv',
            "9":'wxyz'
        }
        ans=[]
        def bt(cur, idx):
            if len(idx) == 0:
                ans.append(cur)
            else:
                for c in mapping[idx[0]]:
                    bt(cur + c, idx[1:])

        bt("", digits)
        return ans 

        