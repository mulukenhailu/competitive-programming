class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        u=len(nums)-1
        while l<=u:
            mid=(l+u)//2
            if nums[mid]==target:
                return mid
            else:
                if nums[mid]<target:
                    l=mid+1
                else:
                    u=mid-1
        if target > nums[mid]:
            return mid+1
        else:
            return mid
        