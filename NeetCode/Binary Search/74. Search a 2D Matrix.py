from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col0 = [row[0] for row in matrix]

        left, right = 0, len(col0) - 1

        while left <= right:
            mid = (left + right) // 2
            
            if col0[mid] == target:
                return True
            elif col0[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        row0 = matrix[left-1] 
        left, right = 0, len(row0) - 1

        while left <= right:
            mid = (left + right) // 2
            
            if row0[mid] == target:
                return True
            elif row0[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False

# Time: O(log m + log n) where m is number of rows and n is number of columns
# Space: O(m) where m is number of rows
# Example usage:
sol = Solution()
print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))  # Output: True