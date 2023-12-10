class Solution:
    def largestOddNumber(self, num: str) -> str:

        if int(num[-1])%2!=0:
            return num
        else:
            num=num[-1::-1]
            ans=""
            for i, n in enumerate(num):
                if int(n)%2!=0:
                    ans=num[i:]
                    print(ans)
                    return ans[-1::-1]
            else:
                return ""
                
            
                
        