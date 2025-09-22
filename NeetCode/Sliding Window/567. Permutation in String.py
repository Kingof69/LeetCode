from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False

        need = Counter(s1)
        window = Counter(s2[:n])

        if window == need:
            return True

        for i in range(n, m):
            window[s2[i]] += 1              # thêm ký tự mới vào window
            window[s2[i-n]] -= 1            # loại ký tự cũ ra khỏi window

            if window[s2[i-n]] == 0:        # dọn key rác để so sánh cho chuẩn
                del window[s2[i-n]]

            if window == need:
                return True

        return False

# Example usage:
solution = Solution()
print(solution.checkInclusion("ab", "eidbaooo"))  # Output: True
print(solution.checkInclusion("ab", "eidboaoo"))  # Output: False