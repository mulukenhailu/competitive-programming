class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dictt=defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if (i+j) in dictt:
                    dictt[i+j].append((i, j))
                else:
                    dictt[i+j]=[(i, j)]
        for k, v in dictt.items():
            if k%2==0:
                dictt[k]=v[::-1]
                
        print(dictt)
        ans=[]
        for v in dictt.values():
            for t in v:
                i, j = t
                ans.append(mat[i][j])
                
        print(ans)
        
        return ans
              
            
        
        
        
        
        
        
        
        
#         ans=[]
#         seen=set()
#         for i in range(len(mat)):
#             for j in range(len(mat[0])):
#                 print(i, j)
#                 ans.append((i, j))
#                 r=i 
#                 c=j
#                 while r+1>-1 and r+1<len(mat) and c-1>-1 and c-1<len(mat):
#                     if (r+1, c-1) not in seen:
#                         print(r+1, c-1)
#                         ans.append((r+1, c-1))
#                         r+=1
#                         c-=1
#         ans2=[]
#         for t in ans:
#             if t not in ans2:
#                 ans2.append(t)
        
#         for t in ans2:
#             i, j=t
#             temp=[]
#             while (i+j)%2==0:
#                 temp.append((i, j))
#             temp.reverse()
#             print(temp)
#             temp=[]
                