class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lst=set()
        num=nums.sort()
        for i in range(len(nums)):
            num=sorted(nums)[:]
            base=num[i]
            l=i+1
            r=len(num)-1
            target=0-base
            while l < r: 
                if num[l]+num[r] == target:
                    if (base, num[l], num[r]) not in lst:
                        lst.add((base, num[l], num[r]))
                    l+=1
                    r-=1 
                elif num[l]+num[r]<target:
                    l+=1
                elif num[l]+num[r]>target:
                    r-=1
                elif l == r:
                    return 
                else:
                    if (base, num[l], num[r]) not in lst:
                        lst.add((base, num[l], num[r]))
        return lst