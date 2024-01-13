class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        ans=[]

        if not firstList or not secondList:
            return []

        for i in range(len(firstList)):
            for j in range(len(secondList)):
                x1, y1=firstList[i]
                x2, y2=secondList[j]
                
                if x1<=x2<=y1<=y2:
                    ans.append([x2, y1])
                    continue
                elif x2<=x1<=y2<=y1:
                    ans.append([x1, y2])
                    continue
                elif x2<=x1<=y1<=y2:
                    ans.append([x1, y1])
                elif x1<=x2<=y2<=y1:
                    ans.append([x2, y2])

        print(ans)  
        return ans       