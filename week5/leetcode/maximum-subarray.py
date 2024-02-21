class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # brute force not acceptable
        # ans=float("-inf")
        # for i in range(len(nums)):
        #     cursum=0
        #     for j in range(i, len(nums)):
        #         cursum+=nums[j]
        #         ans=max(ans, cursum)

        # return ans

        # Dp
        # n=len(nums)
        # maxSumEnd=[0]*n
        # maxSumEnd[0]=nums[0]

        # for i in range(1, n):
        #     if maxSumEnd[i-1]>0:
        #         maxSumEnd[i]=maxSumEnd[i-1]+nums[i]
        #     else:
        #         maxSumEnd[i]=nums[i]

        # ans=float("-inf")
        # for i in range(n):
        #     ans=max(ans, maxSumEnd[i])

        # return ans

        # kadanes Algo
        n=len(nums)
        ans=nums[0]
        maxSumEnd=nums[0]

        for i in range(1, n):
            maxSumEnd=max(maxSumEnd+nums[i], nums[i])
            ans=max(ans, maxSumEnd)
        
        return ans
        

            
        
        
        