from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1
    
# Time: O(log n)
# Space: O(1)
# Example usage:
sol = Solution()
print(sol.search([-1,0,3,5,9,12], 9))  # Output: 4