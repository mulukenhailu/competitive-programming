class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        ans=0
        seen=set()
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j and nums[i]+nums[j]<target:
                    if (i, j) not in seen and (j, i) not in seen:
                        ans+=1
                seen.add((i, j))
        return ans

        