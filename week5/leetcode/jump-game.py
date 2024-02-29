class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True

        max_reachable = 0
        for i in range(n):
            if max_reachable < i:
                return False
            max_reachable = max(max_reachable, i + nums[i])

            if max_reachable >= n - 1:
                return True

        return False
