class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        ans=[]
        totalsum=sum(nums)
        presum=0

        for i, n in enumerate(nums):
            left=n*i-presum
            right=totalsum-presum-n*(len(nums) - i)

            ans.append(left+right)
            presum+=n
        
        return ans