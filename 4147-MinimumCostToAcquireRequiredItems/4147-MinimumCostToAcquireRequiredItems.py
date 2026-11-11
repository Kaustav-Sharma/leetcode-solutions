# Last updated: 11/11/2026, 4:43:54 pm
class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        c=0
        d=False
        if need1>need2:
            d=True
        if cost1+cost2>costBoth:
            if d:
                c=need2*costBoth
                c+=(need1-need2)*min(cost1,costBoth)
            else:
                c=need1*costBoth
                c+=(need2-need1)*min(cost2,costBoth)
        else:
            c=need1*cost1 + need2*cost2
        return c
            