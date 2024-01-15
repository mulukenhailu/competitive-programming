class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        p1=0
        p2=0

        while p1<len(name) and p2<len(typed):

            if name[p1]!=typed[p2]:
                return False

            c1=0
            while p1+1<len(name) and name[p1]==name[p1+1]:
                p1+=1
                c1+=1

            
            c2=0
            while p2+1<len(typed) and typed[p2]==typed[p2+1]:
                p2+=1
                c2+=1

            if c2<c1:
                return False

            p2+=1
            p1+=1
            c1=0
            c2=0

        if p1<len(name) or p2<len(typed):
            return False

        else:
            return True

        
    



