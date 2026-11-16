class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []

        def dfs(index, current, sum):
            if sum == target:
                output.append(current.copy())
                return 

            if index >= len(nums) or sum > target:
                return

            current.append(nums[index])
            dfs(index, current, sum + nums[index])
            current.pop()
            dfs(index + 1, current, sum)
        
        dfs(0, [], 0)
        return output