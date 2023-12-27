class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = ""
        for i in range(0, len(s), 2*k):
            temp = s[i:i+2*k]
            ans += temp[0:k][::-1]+temp[k:] 
        return ans