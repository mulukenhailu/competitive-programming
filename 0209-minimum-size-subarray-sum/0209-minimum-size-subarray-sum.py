class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        r=0
        Csum=0
        min_len=float("inf")
        while l<len(nums):
            if r<len(nums) and Csum<target:
                Csum+=nums[r]
                r+=1
            elif Csum>=target:
                min_len=min(min_len, r-l)
                Csum-=nums[l]
                l+=1
            else:
                break
        if min_len==float("inf"):
            return 0
        else:
            return min_len
        
        
                
            
        
            
            
            