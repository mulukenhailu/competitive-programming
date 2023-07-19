class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        ans=0
        p1, p2=0, 0
        while p1<len(players) and p2<len(trainers):
            if players[p1]<=trainers[p2]:
                p1+=1
                p2+=1
                ans+=1
            elif players[p1]>trainers[p2]:
                p2+=1
            else:
                p1+=1
        return ans  # time O(nlogn) space O(1)
                