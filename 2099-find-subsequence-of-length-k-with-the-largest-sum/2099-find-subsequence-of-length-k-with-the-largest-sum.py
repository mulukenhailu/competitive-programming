class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        ans=[]
        for i, num  in enumerate(nums):
            heappush(heap, (num, i))
            if len(heap)>k:
                heappop(heap)
        heap.sort(key=lambda x :x[1])
        for t in heap:
            ans.append(t[0])
        return ans