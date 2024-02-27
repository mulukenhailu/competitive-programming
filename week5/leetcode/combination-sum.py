class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]

        def bt(arr, cursum, idx):
            if cursum>target:
                return 

            if cursum==target:
                ans.append(arr[:])
                return 

            for i in range(idx, len(candidates)):
                arr.append(candidates[i])
                bt(arr, cursum+candidates[i], i)
                arr.pop()

        bt([], 0, 0)
        return ans