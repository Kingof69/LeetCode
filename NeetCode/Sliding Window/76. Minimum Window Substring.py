from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)       # Đếm số ký tự cần
        window = Counter()
        
        have, need_count = 0, len(need)   # số ký tự đã thỏa mãn / cần thỏa mãn
        res, res_len = [-1, -1], float("inf")
        
        l = 0
        for r, ch in enumerate(s):
            window[ch] += 1
            
            if ch in need and window[ch] == need[ch]:
                have += 1
            
            while have == need_count:
                # update kết quả ngắn nhất
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                
                # Thu hẹp cửa sổ từ bên trái
                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return "" if res_len == float("inf") else s[l:r+1]
    
# Example usage:
solution = Solution()
print(solution.minWindow("ADOBECODEBANC", "ABC"))  # Output: "BANC"
print(solution.minWindow("a", "a"))                # Output: "a"