class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
#          0          1        2         3    4
#                              1         2    3
#         -1          2        2         3    3   
#          c=5       c=3      c=1       c=2   c=2
#          s=0       s=1      s=2       s=7   s=14
        
#         (1,4)==>123
#         2==>(2+1)+(1+1)
#           2=(i-(i-1))

#                 1       2   3       4       5
    
#         1       1       1   4       2        3
#         c=3     c=2    c=1  c=0     c=2      c=1
#         s=1     s=2    s=3  s=10    s=19     s=30
    
    
        c=capacity-plants[0]
        step=1
        
        for i in range(1, len(plants)):
            if c>=plants[i]:
                c-=plants[i]
                step+=1
            elif c<plants[i]:
                c=capacity-plants[i]
                step+=(2*i+1)
        return step
                
                