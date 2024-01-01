class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans=0
        for r in range(len(mat)):
            for c in range(len(mat)):
                if r==c or r+c==len(mat)-1:
                    ans+=mat[r][c]
        return ans