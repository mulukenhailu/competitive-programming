class Solution:
    def isPalindrome(self, s: str) -> bool:
        words=list(s)
        news=''
        for word in words:
            if word.isalnum() == True:
                news+=word 
        checkpali=news.lower()
        left=0
        right=len(checkpali)-1
        if len(s)==0:
            return True
        while left < right:
            if checkpali[left] == checkpali[right]:
                left+=1
                right-=1
            else:
                return False
        return True