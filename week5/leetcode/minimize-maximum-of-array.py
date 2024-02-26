class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        cursum=nums[0]
        ans=nums[0]

        for i in range(1, len(nums)):
            cursum+=nums[i]
            ans=max(ans, math.ceil(cursum/(i+1)))

        return ans
        