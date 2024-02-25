class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        temp=list(palindrome)

        if len(palindrome)==1:
            return ""
        
        for i in range(len(temp)//2):
            if temp[i] != "a":
                temp[i]="a"
                break
        else:
            temp[-1]="b"

        return "".join(temp)