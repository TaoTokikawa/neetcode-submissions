class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_side = [0] * len(nums)
        right_side = [0] * len(nums)
        prod = [0] * len(nums)
        left_side[0] = right_side[len(nums) - 1] = 1
        for i in range(1, len(nums)):
            left_side[i] = nums[i - 1] * left_side[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            right_side[i] = nums[i + 1] * right_side[i + 1]
        
        for i in range(0, len(nums)):
            prod[i] = left_side[i] * right_side[i]

        return prod