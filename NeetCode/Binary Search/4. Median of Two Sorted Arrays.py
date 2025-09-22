from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = nums1 + nums2      # gộp 2 mảng
        a.sort()               # sắp xếp
        m = len(a)

        if m % 2 == 1:  # số phần tử lẻ
            return float(a[m // 2])
        else:           # số phần tử chẵn
            return (a[m // 2 - 1] + a[m // 2]) / 2.0
        
# Example usage:
solution = Solution()
print(solution.findMedianSortedArrays([1, 3], [2]))  # Output: 2.0