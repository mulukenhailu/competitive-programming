class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        lst=nums[:]
        nums.sort()
        nums=list(set(nums))
        if len(nums)<3:
            return max(lst)
        nums.sort()   
        for _ in range(2):
            nums.pop()
        return nums[-1]
        
        
           # heap=[]
        # for num in nums:
        #     heapq.heappush(heap, -num)
        # heap=list(set(heap))
        # if len(heap)<3:
        #     return -min(heap)
        # else:
        #     for _ in range(2):
        #         heapq.heappop(heap)
        # return -heap[0]