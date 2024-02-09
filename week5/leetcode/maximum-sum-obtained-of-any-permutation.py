class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n=len(nums)
        inital=[0]*n

        for r in requests:
            s, e=r
            inital[s]+=1
            if e+1<n:
                inital[e+1]-=1

        presum=[inital[0]]
        for i in range(1, n):
            presum.append(presum[-1]+inital[i])

        presum.sort()
        nums.sort()
        ans=0
        for p, n in zip(presum, nums):
            ans+=p*n

        return ans%((10**9)+7)
        