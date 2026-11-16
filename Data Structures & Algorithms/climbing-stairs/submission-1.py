class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * n
        def dfs(current):
            if current == n:
                return 1
            elif current > n:
                return 0
            
            if dp[current] != -1:
                return dp[current]
            
            dp[current] = dfs(current + 1) + dfs(current + 2)

            return dp[current]

        return dfs(0)
