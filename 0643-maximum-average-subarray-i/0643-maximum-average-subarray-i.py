class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        pre_sum=sum(nums[:k])
        pre_sum_copy=pre_sum
        for num in range(len(nums)-k):
            pre_sum=pre_sum-nums[num]+nums[num+k]
            pre_sum_copy=max(pre_sum_copy, pre_sum)
        return pre_sum_copy/k   # time O(n) space O(n)
