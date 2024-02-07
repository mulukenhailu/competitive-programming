class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        inital=[0]*len(s)

        for sh in shifts:
            l, r, d=sh

            if d==0:
                inital[l]-=1
                if r+1<len(s):
                    inital[r+1]+=1
            else:
                inital[l]+=1
                if r+1<len(s):
                    inital[r+1]-=1

        presum = [inital[0]]

        for i in range(1, len(inital)):
            presum.append((presum[-1] + inital[i]))  


        print(presum)
        ans=""
        for i in range(len(presum)):
            shi=(((ord(s[i])+presum[i])-97)%26)+97
            ans+=chr(shi)


        return ans
        


        
        

        