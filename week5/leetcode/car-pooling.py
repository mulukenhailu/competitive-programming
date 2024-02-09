class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        rnge=0
        for tt in trips:
            p, f, t=tt
            rnge=max(rnge, t)

        print(rnge)

        inital=[0]*(rnge+1)
        for  tt in trips:
            pas, fr, to=tt
            inital[fr]+=pas
            if to<rnge:
                inital[to]-=pas
        
        print(inital)

        presum=[inital[0]]
        for i in range(1, len(inital)):
            presum.append(presum[-1]+inital[i])

        print(presum)
        
        return max(presum)<=capacity