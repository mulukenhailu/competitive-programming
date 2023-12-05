class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        ans1=""
        ans2=""
        for w in word1:
            ans1+=w
        for w in word2:
            ans2+=w
        return ans1==ans2
            
        