class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        pos=[]
        for stend in ranges:
            for r in range(stend[0], stend[1]+1):
                pos.append(r)
        
        for num in  range(left, right+1):
            if num not in pos:
                return False
        return True
        