class Solution:
    def minimumSteps(self, s):
        ans=0
        step=0
        n=len(s)
        for i in range(n):
            if s[i] == '0':
                ans += step
            else:
                step += 1
        return ans

