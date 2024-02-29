class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # obj: minimize total cost
        # decision Variable: choose city a or b
        # constraints: exactly move one city
        
        # 1.greedly choose min of the two ...do not work
        # ans=0
        # for c in costs:
        #     p1, p2=c
        #     ans+=min(p2, p1)
        # return ans

        # 2.checkig the profit
        # loss of moving to A
        lossA=[]
        for i, c in enumerate(costs):
            p1, p2=c
            lossA.append([[p1-p2], i])

        lossA.sort(key=lambda x:x[0])
        print(lossA)

        ans=0
        n=len(costs)
        for i in range(n):
            loss, idx=lossA[i]
            if i<(n/2):
                ans+=costs[idx][0]
            else:
                ans+=costs[idx][1]
        
        return ans
        

