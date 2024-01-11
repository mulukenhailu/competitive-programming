class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:

        seen=set()
        min_len=float("inf")
        l=0

        for r in range(len(cards)):

            if cards[r] in seen:
                while cards[l]!=cards[r]:
                    seen.remove(cards[l])
                    l+=1
                min_len=min(min_len, r-l+1)
                l+=1
            
            seen.add(cards[r])

        print(min_len)
        return min_len if min_len!=float("inf") else -1
                
        