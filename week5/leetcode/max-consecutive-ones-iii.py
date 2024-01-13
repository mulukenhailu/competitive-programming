class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        pos=0
        ans=0

        for r in range(len(nums)):
            if nums[r]==0:
                pos+=1
            
            while pos>k:
                ans=max(ans, r-l)
                if nums[l]==0:
                    pos-=1
                l+=1

        return max(ans, r-l+1)

        