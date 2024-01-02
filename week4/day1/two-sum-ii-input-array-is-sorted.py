class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        while l < r :
            if numbers[l]+numbers[r]<target:
                l+=1
            elif numbers[l]+numbers[r]>target:
                r-=1
            else:
                return [l+1, r+1]
        #or
        # for i in range(len(numbers)):
        #     diff=target-numbers[i]
        #     left=0
        #     right=len(numbers)
        #     while left < right:
        #         mid=(left+right)//2
        #         if numbers[mid]>diff:
        #             right=mid
        #         elif numbers[mid]<diff:
        #             left=mid+1
        #         else:
        #             if i != mid:
        #                 return [i+1, mid+1]
        #             else:
        #                 if numbers[i]==numbers[i+1]:
        #                      return [i+1, mid+2]