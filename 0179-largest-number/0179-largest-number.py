import functools 

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(num1, num2):
            if int(num1 + num2) < int(num2 + num1):
                return True
            return False
        
        nums = list(map(str, nums))
        n = len(nums)
        for _ in range(n):
            for j in range(n-1):
                if compare(nums[j], nums[j+1]):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        
        return str(int("".join(nums)))
        