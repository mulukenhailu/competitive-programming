class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 1124 78
        # 11241......111 24
        # 11 12
        # 1 11
        # 1
        for i, s in enumerate(stones):
            stones[i] = -s
        heapify(stones)
        while stones:
            s1 = -heappop(stones)
            if len(stones)==0:
                return s1
            s2=-heappop(stones)         
            if s1!=s2:
                heappush(stones, s2-s1)
        return 0
