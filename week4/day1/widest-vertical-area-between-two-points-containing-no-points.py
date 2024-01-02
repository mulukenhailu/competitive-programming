class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        pts=set()

        for p in points:
            if p[0] not in pts:
                pts.add(p[0])

        pts=list(pts)
        pts.sort()
        ans=float("-inf")

        for i in range(len(pts)-1):
            ans=max((pts[i+1]-pts[i]), ans)

        if ans!=float("-inf"):
            return ans
        return 0

        
