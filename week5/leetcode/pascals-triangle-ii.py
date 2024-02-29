class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        def pascal(r):
            if r==1:
                return [1, 1]

            lst=pascal(r-1)
            ans=[1]
            for i in range(1, len(lst)):
                ans.append(lst[i-1]+lst[i])
            ans+=[1]
            return ans

        return pascal(rowIndex)