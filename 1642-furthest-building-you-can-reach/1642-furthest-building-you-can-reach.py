class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # for i in range(len(heights)):
        #     if bricks == 0 and ladders == 0:
        #         return i
        #     if heights[i] >= heights[i + 1]:
        #         continue
        #     elif heights[i] < heights[i + 1] and bricks >= heights[i + 1] - heights[i]:
        #         bricks -= heights[i + 1] - heights[i]
        #     else:
        #         ladders -= 1
        jumps= []
        for i in range(len(heights) - 1):
            height = heights[i + 1] - heights[i]
            if height <= 0: continue
            heappush(jumps, height)
            if len(jumps) > ladders:
                bricks -= heappop(jumps)
            if(bricks < 0) : return i
        return len(heights) - 1