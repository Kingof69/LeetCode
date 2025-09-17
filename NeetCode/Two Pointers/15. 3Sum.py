from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # sort cho dễ làm two pointers
        
        n = len(nums)
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue  # bỏ duplicate

            target = -nums[i]
            left, right = i+1, n-1

            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    res.append([nums[i], nums[left], nums[right]])
                    # tránh trùng
                    while left < right and nums[left] == nums[left+1]:
                        left+=1
                    while left < right and nums[right] == nums[right-1]:
                        right-=1
                    left+=1
                    right -= 1
                elif s < target:
                    left+=1
                else:
                    right-=1

        return res
    
print(Solution().threeSum([-1,0,1,2,-1,-4]))
