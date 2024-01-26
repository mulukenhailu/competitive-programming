class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        n=len(nums)
        l=0
        c=0
        temp=0
        ans=0

        for r in range(n):
            if nums[r]%2==1:
                c+=1
                temp=0

            while c==k:
                if nums[l]%2==1:
                    c-=1
                temp+=1
                l+=1
            ans+=temp

        return ans





