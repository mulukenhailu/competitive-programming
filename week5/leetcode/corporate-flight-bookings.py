class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        inital=[0]*(n)

        for b in bookings:
            f, l, s=b
            inital[f-1]+=s
            if l<n:
                inital[l]-=s

        presum=[inital[0]]
        for i in range(1, n):
            presum.append(presum[-1]+inital[i])

        return presum
        