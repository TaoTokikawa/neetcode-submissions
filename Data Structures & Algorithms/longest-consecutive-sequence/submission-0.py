class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_cons = 0

        for i in range(len(nums)):
            if nums[i] - 1 not in nums_set:
                temp_count = 1
                while True:
                    if nums[i] + temp_count in nums_set:
                        temp_count += 1
                    else:
                        break
                max_cons = max(temp_count, max_cons)
        
        return max_cons