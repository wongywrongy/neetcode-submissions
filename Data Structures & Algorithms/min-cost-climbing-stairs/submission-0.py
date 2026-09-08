class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        next1, next2 = 0, 0

        for i in range(n-1, -1, -1):
            cur = cost[i] + min(next1, next2)
            next2 = next1
            next1 = cur

        return min(next1, next2)