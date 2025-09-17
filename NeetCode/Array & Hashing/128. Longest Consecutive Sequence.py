from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = sorted(set(nums))  # sort + bỏ trùng
        longest = 1
        count = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                count += 1
                longest = max(longest, count)
            else:
                count = 1  # reset vì bị ngắt dãy

        return longest
