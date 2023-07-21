class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        sc = Counter(s[:len(p)])  
        pc = Counter(p)

        for i in range(len(p), len(s)):
            if sc == pc:
                ans.append(i - len(p))  
            sc[s[i - len(p)]] -= 1
            sc[s[i]] += 1
        if sc == pc:
            ans.append(len(s) - len(p))
        return ans
        