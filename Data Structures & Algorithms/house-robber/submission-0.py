class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)

        def helper(index):
            if index >= len(nums):
                return 0
            
            if dp[index] != -1:
                return dp[index]
            
            dp[index] = max(nums[index] + helper(index + 2), helper(index + 1))

            return dp[index]
        
        return helper(0)