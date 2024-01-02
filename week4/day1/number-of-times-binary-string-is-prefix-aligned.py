class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        cnt=0
        maxidx=0
        ones=0
        for i in flips:
            maxidx=max(i, maxidx)
            ones+=1
            if ones==maxidx:
                cnt+=1
        return cnt
            
        