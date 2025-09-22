class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        best = 0
        
        for i in range(n):  # bắt đầu tại từng vị trí i
            seen = set()
            length = 0
            for j in range(i, n):  # duyệt tiếp từ i
                if s[j] in seen:
                    break  # gặp trùng thì dừng
                seen.add(s[j])
                length += 1
            best = max(best, length)  # cập nhật kết quả
            
        return best
    
# Example usage:
solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))  # Output: 3
print(solution.lengthOfLongestSubstring("bbbbb"))     # Output: 1