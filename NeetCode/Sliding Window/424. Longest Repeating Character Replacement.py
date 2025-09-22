from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = Counter()
        left = 0
        max_freq = 0
        res = 0

        for right in range(len(s)):
            count[s[right]] += 1
            max_freq = max(max_freq, count[s[right]])

            # nếu cửa sổ không hợp lệ thì thu nhỏ
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res
    
# Example usage:
solution = Solution()
print(solution.characterReplacement("ABAB", 2))  # Output: 4
print(solution.characterReplacement("AABABBA", 1))  # Output: 4