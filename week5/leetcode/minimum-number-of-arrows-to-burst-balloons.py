class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        print(points)

        numsofArrow=1
        arrowPos=points[0][1]

        for p in points:
            x1, x2=p
            if x1 <= arrowPos <= x2:
                pass
            else:
                numsofArrow+=1
                arrowPos=x2

        return numsofArrow

        