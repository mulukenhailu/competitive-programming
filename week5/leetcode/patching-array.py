class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        Firstmiss=1
        ans=0
        i=0

        while Firstmiss<=n:
            if i<len(nums) and nums[i]<=Firstmiss:
                Firstmiss+=nums[i]
                i+=1
            else:
                Firstmiss+=Firstmiss
                ans+=1
        return ans
        