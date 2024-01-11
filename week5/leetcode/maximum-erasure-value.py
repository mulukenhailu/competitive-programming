class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l=0
        seen=set()
        cursum=0
        maxsum=0
        for r in range(len(nums)):

            
            while nums[r] in seen:
                maxsum=max(maxsum, cursum)
                cursum-=nums[l]
                seen.remove(nums[l])
                l+=1

            if nums[r] not in seen:
                cursum+=nums[r]
                seen.add(nums[r])

        print(maxsum, cursum)

        return max(maxsum, cursum)
            

            

            


        