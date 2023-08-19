class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums)==1:
            return nums
        freq=dict(Counter(nums))
        heap=[]
        ans=[]
        for v, f in freq.items():
            heappush(heap, [-f, v])
        for _ in range(k):
            f, v = heappop(heap)
            ans.append(v)
        return ans
            
                    
            
            
            
