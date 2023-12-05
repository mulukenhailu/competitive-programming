class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # 1,1,2,10    
        # 1+1>2=f
        # 1+2>10=f
        
        # 2334
        # 3-2<3<2+3=1<3<5
        # 3-3<4<3+3=0<4<6
        
        nums.sort()
        posPerimeter=[]
        for i in range(len(nums)-2):
            s1, s2, s3=nums[i], nums[i+1], nums[i+2]
            if abs(s2-s1)<s3<abs(s1+s2):
                posPerimeter.append(s1+s2+s3)
        print(posPerimeter)
        if posPerimeter:
            return max(posPerimeter)
        else:
            return 0
                
        
        