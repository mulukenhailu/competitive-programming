class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # ==>f>n/3>1
        # 3:2
        # 2:1
        ans=[]
        tarfeq=len(nums)/3
        nums=Counter(nums)
        print(nums)
        print(tarfeq)
        for k, v in nums.items():
            if v>tarfeq:
                ans.append(k)
        return ans
        
            