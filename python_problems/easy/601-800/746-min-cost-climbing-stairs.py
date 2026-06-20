class Solution:
    def minCost(self, cost, i, memo):
        if i >= len(cost):
            return 0
        if i in memo:
            return memo[i]
        memo[i] = cost[i] + min(self.minCost(cost, i+1, memo), self.minCost(cost, i+2, memo))
        return memo[i]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        return min(self.minCost(cost, 0, memo), self.minCost(cost, 1, memo))
        