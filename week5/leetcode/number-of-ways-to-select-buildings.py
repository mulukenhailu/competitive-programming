class Solution:
    def numberOfWays(self, s: str) -> int:
        ones=s.count("1")
        zeros=s.count("0")

        curones=0
        curzeros=0
        ans=0
        for num in s:
            if num=="1":
                ans+=curzeros*(zeros-curzeros)
                curones+=1
            elif num=="0":
                ans+=curones*(ones-curones)
                curzeros+=1
        return ans