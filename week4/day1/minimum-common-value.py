class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n=len(nums1)
        m=len(nums2)
        p1=0
        p2=0
        while p1<n and p2<m:
            if nums1[p1]==nums2[p2]:
                return nums1[p1]
            elif nums1[p1]<nums2[p2]:
                p1+=1
            else:
                p2+=1
        if p1<n or p2<m:
            return -1

        