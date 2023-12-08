class Solution:
    def minOperations(self, boxes: str) -> List[int]:
#         012345
#         001011
#         0=2-0+4-0+5-0=11
#         1=11-3*1=8
#         2=11-2*3=5
#         3=2-3+4-3+5-3=1+1+2=4
#         4=2-4+5-4=3
#         5=2-5+4-5=4
        
#         2:1
#         4:1
#         5:1
        pos=[] 
        output=[]
        ans=0
        for i in range(len(boxes)):
            if boxes[i]==str(1):
                pos.append(i)
        print(pos)
        for i in range(len(boxes)):
            if i not in pos:
                for p in pos:
                    ans+=abs(p-i)
                output.append(ans)
            
            else:
                for p in pos:
                    if p!=i:
                        ans+=abs(p-i)
                output.append(ans)
                
            ans=0
        return output
            