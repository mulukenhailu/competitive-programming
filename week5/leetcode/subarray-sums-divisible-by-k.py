class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # Dic = {0:1}
        # n = len(nums)
        # ans = 0 
        # s=0
        # for num in nums:
        #     s+=num
        #     temp=(s%k+k)%k
              
        #     if temp in Dic:
        #         ans += Dic[s%k]
            
        #     if temp in Dic:
        #         Dic[temp] +=1
        #     else:
        #         Dic[temp] = 1  
                
        # return ans

        n = len(nums)
        dic = {}
        dic[0] = 1
        ans, prefix = 0, 0
        for a in nums:
            prefix += a
            rem = prefix%k
            if rem in dic:
                ans += dic[rem]
                dic[rem] +=1
            else:
                dic[rem] = 1
        return ans