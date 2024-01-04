class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums_counter=Counter(nums)
        nums.sort()
        seen=set()
        unique=[]

        for num in nums:
            if num not in seen:
                unique.append(num)
                seen.add(num)

        ans=0
        for i, num in enumerate(unique):
            ans+=i*nums_counter[num]
        
        return ans

        