class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left <= right:
            mid = (left + right) // 2
            temp_count = 0
            for n in piles:
                temp_count += math.ceil(float(n) / mid)
            if temp_count > h:
                left = mid + 1
            else:
                right = mid - 1
        return left