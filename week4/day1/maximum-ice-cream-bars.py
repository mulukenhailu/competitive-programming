class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()

        if sum(costs)<coins:
            return len(costs)

        if costs[0]>coins:
            return 0
        
        else:
            cur_sum=0

            for i, c in enumerate(costs):
                cur_sum+=c

                if cur_sum>coins:
                    return i
                elif cur_sum==coins:
                    return i+1
        