from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums.sort()

        return nums[0]

# Example usage:
sol = Solution()
print(sol.findMin([3,4,5,1,2]))  # Output: 1