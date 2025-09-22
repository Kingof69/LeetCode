import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Tốc độ nhỏ nhất có thể: 1 quả/giờ
        # Tốc độ lớn nhất có thể: max(piles)
        low, high = 1, max(piles)
        res = high

        while low <= high:
            mid = (low + high) // 2
            total = 0

            # Tính tổng thời gian cần nếu ăn với speed = mid
            for p in piles:
                total += math.ceil(p / mid)

            if total <= h:
                res = mid   # lưu kết quả tạm
                high = mid - 1  # thử speed nhỏ hơn
            else:
                low = mid + 1   # cần speed lớn hơn

        return res

# Example usage:
sol = Solution()    
print(sol.minEatingSpeed([3,6,7,11], 8))  # Output: 4