from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            min_height = min(height[left], height[right])
            max_area = max(max_area, min_height*(right-left))

            if height[left] == min_height:
                left += 1
            else: 
                right -= 1
        return max_area

height = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(height))