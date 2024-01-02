class Solution:
    def smallestNumber(self, num: int) -> int:
        string=[n for n in str(num)]
        s_count=Counter(string)
        if num > 0:
            string.sort()
            if "0" in string:
                for i in range(len(string)):
                    if string[i]!="0":
                        break
                ans=string[i]
                for _ in range(s_count["0"]):
                    ans+="0"
                for s in string[i+1:]:
                    ans+=s
                return int(ans)
            return int("".join(string))
        
        elif num < 0:
            temp=sorted(string[1:], reverse=True)
            return int("-"+"".join(temp))
        else:
            return 0

