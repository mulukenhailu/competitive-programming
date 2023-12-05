class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(0, len(nums)-1, 2):
            freq, val=nums[i:i+2]
            ans.extend(val for _ in range(freq))
        print(ans)
        return ans
            