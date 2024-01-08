class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        if sum(nums)<target:
            return 0

        l=0
        r=0
        cursum=0
        n=len(nums)
        ans=len(nums)

        while r<n:
            cursum+=nums[r]
            while cursum>=target:
                ans=min(ans, r-l+1)
                cursum-=nums[l]
                l+=1
            r+=1
        
        return ans


        