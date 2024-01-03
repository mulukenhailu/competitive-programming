class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:  
        l=1
        n=len(nums)
        for i in range(1, n):
            temp=nums[l-1]
            if temp!=nums[i]:
                nums[l], nums[i]=nums[i], nums[l]
                l+=1
        return len(nums[:l])

        # 0101122334
        # 0121102334
        # 0123102134
        # 0123402131

        
        