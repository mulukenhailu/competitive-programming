class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def backtrack(perm):
            if len(perm)==len(nums):
                ans.append(perm[:])
                return 

            for num in nums:
                if num not in perm:
                    perm.append(num)
                    backtrack(perm)
                    perm.pop()

        backtrack([])
        return ans

        
            
        