class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in num:
                return [num[diff], i]
            num[nums[i]] = i

        return [] 