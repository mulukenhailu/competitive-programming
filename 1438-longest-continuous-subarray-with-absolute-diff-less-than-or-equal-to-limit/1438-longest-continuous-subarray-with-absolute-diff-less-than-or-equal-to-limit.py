class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        maxi = deque([])
        mini = deque([])
        left = 0

        for num in nums:
            while maxi and num > maxi[-1]:
                maxi.pop()
            while mini and num < mini[-1]:
                mini.pop()

            maxi.append(num)
            mini.append(num)

            if maxi[0] - mini[0] > limit:
                if maxi[0] == nums[left]:
                    maxi.popleft()
                if mini[0] == nums[left]:
                    mini.popleft()
                left += 1
        return len(nums) - left 