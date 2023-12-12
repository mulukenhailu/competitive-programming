class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dic={num:i for i, num in enumerate(nums)}
        print(dic)
            
        for ope in operations:
            if ope[0] in dic:
                nums[dic[ope[0]]]=ope[1]
                dic[ope[1]]=dic[ope[0]]
                dic.pop(ope[0])
        return nums