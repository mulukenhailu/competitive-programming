class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
            
            # 1 2 3 5  4 10 
            #  7 5 8  4
            winset=set()
            lostdict={}
            
            for match in matches:
                winset.add(match[0])
            for match in matches:
                lostdict[match[1]]=lostdict.get(match[1], 0)+1
            for k, v in lostdict.items():
                if lostdict[k]>=2:
                    lostdict[k]=0
                    winset.discard(k)
                    
            lostset=set(k for k, v  in lostdict.items() if v!=0 )
            
            print(winset)
            print(lostset)
            
            wins=list(winset.difference(lostset))
            wins.sort()
            onelose=list(lostset)
            onelose.sort()
            
            
            
            ans=[wins, onelose]
            
            return ans