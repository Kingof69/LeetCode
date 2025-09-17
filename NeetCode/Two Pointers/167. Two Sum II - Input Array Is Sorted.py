from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] < target:
                left += 1
            if numbers[left] + numbers[right] > target: 
                right -= 1
            if numbers[left] + numbers[right] == target:
                break
        
        return [left+1, right+1]
    
print(Solution().twoSum([2,7,11,15], 9))
print(Solution().twoSum([2,3,4], 6))