class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        Dic = {0:1}
        n = len(nums)
        ans = 0 
        s = 0 
        
        for num in nums:
            
            s += num         
            if s-k in Dic:
                ans += Dic[s-k]
            
            if s in Dic:
                Dic[s] +=1
            else:
                Dic[s] = 1  
                
        return ans