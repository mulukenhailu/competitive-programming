class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        totsum = sum(cardPoints)
        window_sum = sum(cardPoints[:n-k])
        ans = totsum - window_sum

        for i in range(n - k, n):
            window_sum = window_sum - cardPoints[i - (n - k)] + cardPoints[i]
            ans = max(ans, totsum - window_sum)

        return ans