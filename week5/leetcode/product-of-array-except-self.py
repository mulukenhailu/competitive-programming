class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [nums[0]]
        suffix = [1] * n
        ans=[]

        for i in range(1, len(nums)):
            prefix.append(prefix[-1]*nums[i])

        suffix[len(nums)-1]=nums[-1]
        for i in range(len(nums)-2, -1, -1):
            suffix[i]=suffix[i+1]*nums[i]

        
        print(prefix)
        print(suffix)

        for i in range(len(nums)):
            if i!=0 and i!=len(nums)-1:
                ans.append(prefix[i-1]*suffix[i+1])
            else:
                if i==0:
                    ans.append(suffix[i+1])
                elif i==len(nums)-1:
                    ans.append(prefix[i-1])

        return ans




    
