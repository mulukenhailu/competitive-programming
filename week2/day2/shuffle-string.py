class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffled=[0]*len(indices)
        for l, i in zip(s, indices):
            shuffled[i]=l
        return "".join(shuffled)
            
            