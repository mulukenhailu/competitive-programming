class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        tot=sum(nums)
        score=[(tot, 0)]
        zeros=0
        ans=[]
        seen=set()
        for i in range(len(nums)):
            if nums[i]==0:
                zeros+=1
            tot-=nums[i]
            s=zeros+tot
            score.append((s, i+1))
                
        score.sort(reverse=True)
        l=score[0][0]
        for t in score:
            if t[1] not in seen and t[0]==l:
                ans.append(t[1])
        return ans
                
            
            
            
            
        