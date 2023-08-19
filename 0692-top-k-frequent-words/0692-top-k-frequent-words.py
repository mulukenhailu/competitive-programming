class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count=Counter(words)
        heap=[[-i[1], i[0]] for i in count.items()]
        heapify(heap)
        ans=[]
        for _ in range(k):
            fre, w=heappop(heap)
            ans.append(w)
        return ans
        