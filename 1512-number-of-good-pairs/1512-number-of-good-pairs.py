class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        nums=Counter(nums)
        ans=0
        for k, v in nums.items():
            if v>1:
                ans+=(v*(v-1))/2
        return int(ans)