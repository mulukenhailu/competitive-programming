class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        ans=float("-inf")
        cursum=0
        temp=[]

        for i in range(m-2):
            for j in range(n-2):
                for r in range(3):
                    for c in range(3):
                        temp.append(grid[i+r][j+c])

                print(temp)

                for idx, t in enumerate(temp):
                    if idx==3  or idx==5:
                        continue
                    else:
                        cursum+=t
                        
                ans=max(ans, cursum)
                temp=[]
                cursum=0
                print("---")
                
        return ans

        