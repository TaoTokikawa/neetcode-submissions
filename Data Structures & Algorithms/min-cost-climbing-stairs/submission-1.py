class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1] * len(cost)

        def dfs(n):
            if n >= len(cost):
                return 0
            
            if dp[n] != -1:
                return dp[n]
            dp[n] = cost[n] + min(dfs(n + 1), dfs(n + 2))

            return dp[n]
        
        return min(dfs(0), dfs(1))