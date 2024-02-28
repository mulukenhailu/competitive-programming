class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        temp=[[i, n] for i, n in enumerate(tickets)]
        
        q=deque()
        ans=0
        for t in temp:
            q.append(t)

        while temp[k][1] != 0:
            ans+=1
            idx, v=q.popleft()
            if idx==k :
                temp[k][1]-=1
            if v>1:
                q.append([idx, v-1])
            
        return ans

            

