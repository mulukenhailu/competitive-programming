class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        nums=nums[::-1]
        n=len(nums)
        ans=0

        print(11//4)
        prevnum=nums[0]
        for i in range(1, n):
            curnum=nums[i]
            if curnum>prevnum:
                res=curnum // prevnum 
                rem=curnum % prevnum
                
                if rem==0:
                    ans+=res-1
                    prevnum=curnum//res
                else:
                    prevnum=curnum//(res+1)
                    ans+=res
            else:
                prevnum=nums[i]
        
        return ans


        