class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
#         1 2 2 6 6 6 6 7 10  n=9
#         9/9*100=100
#         4/9*100=44.44
        
#         f/n*100>25/100
        
        arrCounter=Counter(arr)
        for k, v in arrCounter.items():
            if (v*100)/len(arr)>25:
                return k
        