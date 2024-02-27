class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]

        def bt(cur, idx):
           
            ans.append(cur[:])

            for c in range(idx, len(nums)):
                cur.append(nums[c])
                bt(cur, c+1)
                cur.pop()

        bt([], 0)

        return ans