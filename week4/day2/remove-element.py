class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        s=0
        f=0
        n=len(nums)

        while f<n:
            if nums[f]!=val:
                nums[s], nums[f]=nums[f], nums[s]
                s+=1
            f+=1
            
        return s
        