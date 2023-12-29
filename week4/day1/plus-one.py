class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans=0
        for i, d in enumerate(digits[::-1]):
            ans+=d*(10**i)
        ans+=1
        return [int(d) for d in str(ans)]





        