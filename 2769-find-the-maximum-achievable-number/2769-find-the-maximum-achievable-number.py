class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        # 1=-1, 3   -2 2
        # 2=1, 3    -1 1
        # 4=3, 5     1  1
        # 5=3, 7     -2 2
        
        # 3=2, 4
        # 5=4, 6
        
        # -1=-3, 1
        # 0=-1, 1
        # 2=1, 3
        # 3=1, 5
        
        pos=[]
        incdec=[]
        ans=[]
        
        for i in range(-t, t+1):
            if i==0:
                continue
            incdec.append(i)
        
        for i in range((num-t), (num+t)+1):
            if i != num:
                pos.append(i)
            
        print(incdec)
        print(pos)
        
        for p, op in zip(pos, incdec):
            ans.append(p-op)
            ans.append(p+op)
            
        print(ans)
        
        return max(ans)
            