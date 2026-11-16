class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        prod_left = [1] * len(nums)
        for i in range(len(nums)):
            prod_left[i] *= left
            left *= nums[i]
        
        right = 1
        prod_right = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            prod_right[i] *= right
            right *= nums[i]
        
        output = []
        for i in range(len(nums)):
            output.append(prod_left[i] * prod_right[i])
        return output