class Solution:
  def maxScore(self, s: str) -> int:
    ans = 0
    zerosCount = 0
    OnesCount = s.count('1')

    for i in range(len(s) - 1):

        if s[i] == '0':
            zerosCount += 1
        else:
            OnesCount -= 1
        temp=zerosCount + OnesCount
        ans = max(ans, temp)

    return ans