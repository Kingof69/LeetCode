from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        indexed_nums.sort(key=lambda x: x[0])

        l, r = 0, len(indexed_nums) - 1
        

        while l <= r:
            mid = (l+r)//2

            if indexed_nums[mid][0] == target:
                return indexed_nums[mid][1] 
            elif indexed_nums[mid][0] < target:
                l = mid+1
            else: 
                r = mid-1
        
        return -1

# Example usage:
sol = Solution()
print(sol.search([4,5,6,7,0,1,2], 0))  # Output: 4
print(sol.search([4,5,6,7,0,1,2], 3))  # Output: -1