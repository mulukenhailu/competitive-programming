class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        equal=[]
        greater=[]
        less=[]
        
        for n in nums:
            if n<pivot:
                less.append(n)
            elif n>pivot:
                greater.append(n)
            else:
                equal.append(n)
        print(equal, greater, less)
        
        less.extend(equal)
        less.extend(greater)
        
        return less