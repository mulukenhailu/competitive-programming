class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        res=[]
        for x, y in points:
            heap.append([x**2+y**2, x, y])

        heap.sort(key=lambda x:x[0],) 

        print(heap)

        for i in range(k):
            res.append([heap[i][1], heap[i][2]])
        return res
            