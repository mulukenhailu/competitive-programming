class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l1=0
        pos=0
        ans1=0
        for r1 in range(len(answerKey)):
            if answerKey[r1]=="F":
                pos+=1

            while pos>k:
                ans1=max(ans1, r1-l1)
                if answerKey[l1]=="F":
                    pos-=1
                l1+=1

        print(r1-l1+1)
        ans1=max(ans1, r1-l1+1)


        l2=0
        pos2=0
        ans2=0

        for r2 in range(len(answerKey)):
            if answerKey[r2]=="T":
                pos2+=1

            while pos2>k:
                ans2=max(ans2, r2-l2)
                if answerKey[l2]=="T":
                    pos2-=1
                l2+=1
            
        print(r2-l2+1)
        ans2=max(ans2, r2-l2+1)

        return max(ans1, ans2)

        
        