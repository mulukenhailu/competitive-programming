class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
#         10...01==00, 01=2=1+1
#         03...01==03, 02, 01=2=0+2
#         00...01==01=1=0+1
        
#         10..20=1+0=1
#         00..20=2+0=2
        
#         20..10=1+0=1
#         00..10=1+0=1
        
        tx, ty=target
        pos=[]
        
        #possible ghost move
        for ghost in ghosts:
            x, y=ghost
            pos.append(abs(tx-x)+abs(ty-y))
        print(pos)
        
        #possible movement of the player
        player=abs(tx)+abs(ty)
        return player<min(pos)
            
            