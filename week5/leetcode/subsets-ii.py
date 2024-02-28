class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=set()
        n=len(nums)
        def bt(cur, idx):
            ans.add(tuple(sorted(cur[:])))

            if idx>=n:
                return 
            
            for i in range(idx, len(nums)):
                cur.append(nums[i])
                bt(cur, i+1)
                cur.pop()
                
        bt([], 0)

        return ans

        