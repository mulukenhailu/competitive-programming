class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        ans=[]
        for n in nums:
            if -1*n==abs(n):
                neg.append(n)
            else:
                pos.append(n) 
                
        for p, n in zip(pos, neg):
            ans.append(p)
            ans.append(n)
        return ans
            
                
        