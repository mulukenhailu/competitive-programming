class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        s1="qwertyuiop"
        s2="asdfghjkl"
        s3="zxcvbnm"
        ans=[]
        for w in words:
            if w[0].lower() in s1:
                checker=s1
            elif w[0].lower() in s2:
                checker=s2
            else:
                checker=s3
            for l in w[1:]:
                if l.lower() not in checker:
                    break
            else:
                ans.append(w)
        print(ans)
        return ans

                    
                