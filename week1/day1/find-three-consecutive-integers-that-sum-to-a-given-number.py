class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        x=(num-3)/3
        if x == int(x):
            x=int(x)
            return [x, x+1, x+2]
        else:
            return []