class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningsum = []
        for i, num in enumerate(nums):
            if i == 0:
                runningsum.append(num)
            else:
                sum_so_far = num + runningsum[-1]
                runningsum.append(sum_so_far)
        return runningsum


        