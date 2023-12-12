class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # =6
        # 1234
        # 2234=8=6+2
        # 2-134=6=8-2
        # -2-134=2=6+(-2-2)
        # -2-136=2+(6-4)=4
        # -2-156=4
        
    
        ans=[]
        cur_even_sum=sum([num for num in nums if num%2==0])
        print(cur_even_sum)
        
        for q in queries:
            idx=q[1]
            val=q[0]
            preNum=nums[idx]
            NewNum=nums[idx]+val
            if NewNum%2==0 and preNum%2!=0:
                ans.append(cur_even_sum+NewNum)
                cur_even_sum+=NewNum
                nums[idx]=NewNum
            elif NewNum%2==0 and preNum%2==0:
                ans.append(cur_even_sum+(NewNum-preNum))
                cur_even_sum+=(NewNum-preNum)
                nums[idx]=NewNum
            elif NewNum%2!=0 and preNum%2==0:
                ans.append(cur_even_sum-preNum)
                cur_even_sum-=preNum
                nums[idx]=NewNum
            else:
                ans.append(cur_even_sum)
                nums[idx]=NewNum
        return ans
            
            