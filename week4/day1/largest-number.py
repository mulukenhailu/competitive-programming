class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        string = [str(num) for num in nums]
        c=0
        for i in range(n):
            for j in range(i, len(string)):
                temp1 = string[i] + string[j]
                temp2 = string[j] + string[i]
                if int(temp2) > int(temp1):
                    string[i], string[j] = string[j], string[i]

        for i in range(len(string)):
            if nums[i] == 0:
                c += 1
            if c == n:
                return "0"

        return "".join(string)
        