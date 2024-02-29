class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        Rq=deque()
        Dq=deque()
        n=len(senate)

        for i in range(n):
            if senate[i]=="R":
                Rq.append(i)
            else:
                Dq.append(i)

        while Rq and Dq:
            ridx, didx=Rq.popleft(), Dq.popleft()
            if ridx < didx:
                Rq.append(ridx+n)
            else:
                Dq.append(didx+n)

        return "Dire" if Dq else "Radiant"
        