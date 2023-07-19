class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        i=0
        j=0
        ans=""
        while i<len(word1) or j<len(word2):
            if i<len(word1) and j<len(word2):
                if word1[i:]>=word2[j:]:
                    ans+=word1[i]
                    i+=1
                if word2[j:]>=word1[i:]:
                    ans+=word2[j]
                    j+=1
            elif i<len(word1):
                ans+=word1[i]
                i+=1
            elif j<len(word2):
                ans+=word2[j]
                j+=1
        return ans
                