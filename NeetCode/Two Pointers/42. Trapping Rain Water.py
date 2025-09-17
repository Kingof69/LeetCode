from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_left = max_right = 0
        water = 0
        
        while l < r:
            if height[l] < height[r]:
                if height[l] >= max_left:
                    max_left = height[l]
                else:
                    water += max_left - height[l]
                l += 1
            else:
                if height[r] >= max_right:
                    max_right = height[r]
                else:
                    water += max_right - height[r]
                r -= 1
        return water

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(Solution().trap(height))