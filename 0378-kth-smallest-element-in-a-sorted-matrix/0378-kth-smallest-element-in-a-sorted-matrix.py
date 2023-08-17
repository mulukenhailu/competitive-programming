class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # count=0
        # while True:
        #     for i, num in enumerate(matrix):
        #         for n in range(len(num)):
        #             count+=1
        #             if count==k:
        #                 return matrix[i][n]
        heap=[]
        for r in matrix:
            for c in r:
                if len(heap)<k:
                    heappush(heap, -c)
                else:
                    if -c > heap[0]:
                        heapreplace(heap, -c)
        return -heap[0]
                
        