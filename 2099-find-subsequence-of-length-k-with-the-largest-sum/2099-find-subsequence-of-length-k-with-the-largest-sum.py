class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # heap=[]
        # ans=[]
        # for num in nums:
        #     heapq.heappush(heap, -num)
        # for _ in range(k):
        #     p=heapq.heappop(heap)
        #     ans.append(-p)
        # return ans
        while len(nums) > k:
            nums.remove(min(nums))
        return nums
    
        