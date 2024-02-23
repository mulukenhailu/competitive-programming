class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        n = len(nums)

        for left in range(n - 2):
            right1 = left + 1
            for right2 in range(left + 2, n):
                while right1 < right2 and nums[left] + nums[right1] <= nums[right2]:
                    right1 += 1
                count += right2 - right1

        return count
