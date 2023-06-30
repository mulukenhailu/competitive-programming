class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic={}
        i=0
        res=0
        for j in range(len(s)):
            while s[j] in dic:
                del dic[s[i]]
                i+=1
            dic[s[j]]=j
            res=max(res, j-i+1)
        return res
              