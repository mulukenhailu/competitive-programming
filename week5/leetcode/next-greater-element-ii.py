class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nextgreater=[]
        ans=[-1]*len(nums)
        for j in range(2):
            for i,num in enumerate(nums):
                    while nextgreater and nums[i] > nums[nextgreater[-1]]:
                            ans[nextgreater.pop()]=nums[i]
                    nextgreater.append(i) 
        return ans