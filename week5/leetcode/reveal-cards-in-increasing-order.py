class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n=len(deck)
        q=deque()

        for i in range(n):
            q.append(i)

        ans=[0]*n
        i=0
        while q:
            ans[q.popleft()]=deck[i]
            if q:
                q.append(q.popleft())
            i+=1

        return ans