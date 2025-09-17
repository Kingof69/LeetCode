from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        # Bước 1: tính tích bên trái (prefix product)
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
 
        # Bước 2: nhân thêm tích bên phải (suffix product)
        suffix = 1
        for i in range(n-1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer