class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 1124 78
        # 11241......111 24
        # 11 12
        # 1 11
        # 1
        
        while True:
            if len(stones)==1:
                return stones[0]
            stones.sort()
            x, y=stones[-2], stones[-1]
            if x==y:
                stones.pop()
                stones.pop()
                if len(stones)==0:
                    stones.append(0)
            else:
                stones.pop()
                stones.pop()
                stones.append(y-x)

                