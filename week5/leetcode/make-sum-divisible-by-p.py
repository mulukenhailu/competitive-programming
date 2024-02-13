class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        k = sum(nums)%p
        dic = {0: -1}

        if k==0:
            return 0

        running=0
        ans = n
      
        for i, num in enumerate(nums):
            running += num
            key = (running%p - k)%p
            if key in dic:
                ans = min(ans, i-dic[key])

            dic[running%p] = i
            
        return ans if ans<n else -1