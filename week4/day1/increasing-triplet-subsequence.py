class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False

        mini = []
        for num in nums:
            if mini and num > mini[-1]:
                mini.append(mini[-1])
            else:
                mini.append(num)

        maxi = []
        for num in nums[::-1]:
            if maxi and num < maxi[-1]:
                maxi.append(maxi[-1])
            else:
                maxi.append(num)
        maxi = maxi[::-1]

        for i in range(1, len(nums) - 1):
            if mini[i] < nums[i] < maxi[i]:
                return True

        return False