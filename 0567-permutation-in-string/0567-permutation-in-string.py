class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1=Counter(s1)
        print(Counter("ab")==Counter("ba"))
        for i in range(len(s2)-len(s1)+1):
            if Counter(s2[i:i+len(s1)]) == Counter(s1):
                return True
        return False
           
        # s1d = {}
        # for c in s1:
        #     s1d[c] = s1d.get(c, 0) + 1  
        # w= {}
        # for i in range(len(s2)):
        #     w[s2[i]] = w.get(s2[i], 0) + 1
        #     if i >= len(s1):
        #         w[s2[i - len(s1)]] -= 1
        #         if w[s2[i - len(s1)]] == 0:
        #             del w[s2[i - len(s1)]]
        #     if w == s1d:
        #         return True
        # return False
        