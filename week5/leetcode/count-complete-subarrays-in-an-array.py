class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n= len(nums) 
        ans=0
        l=0
        count = Counter()
        for r in range(n):
            count[nums[r]] += 1
            while len(count) == len(set(nums)):
                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    del count[nums[l]]
                l += 1
            ans += l
        return ans