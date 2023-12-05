class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        # 11 34 ==>  2, 3=3
        # 34 -10 ==> -4, 4=4
        # -10 06 ==>  1, 6=6
        # 06  99 ==>  9, 3=9
        # 99 10 25 ==> 1, 16=16
        #                   =10+9+3+16=10+16+12=38
        
        time=0
        for i in range(len(points)-1):
            x1, y1=points[i]
            x2, y2=points[i+1]
            xdiff=abs(x2-x1)
            ydiff=abs(y2-y1)
            maxtime=max(xdiff, ydiff)
            time+=maxtime
        print(time)
        return time
            
        