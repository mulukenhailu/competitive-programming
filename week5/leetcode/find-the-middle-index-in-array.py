class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        fp_sum=[nums[0]]

        for num in nums[1:]:
            fp_sum.append(fp_sum[-1]+num)

        nums_rev=nums[::-1]

        rp_sum=[nums_rev[0]]
        for num in nums_rev[1:]:
            rp_sum.append(rp_sum[-1]+num)

        rp_sum=rp_sum[::-1]

        for i in range(len(fp_sum)):
            if fp_sum[i]==rp_sum[i]:
                return i

        return -1

        