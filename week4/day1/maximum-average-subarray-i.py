class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l=0
        cursum=sum(nums[:k])
        maxsum=cursum
        for r in range(k, len(nums)):
            cursum=cursum - nums[l] + nums[r]
            maxsum = max(maxsum, cursum)
            l+=1
        return maxsum/k
