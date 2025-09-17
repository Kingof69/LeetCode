class Solution:
    def isPalindrome(self, s: str) -> bool:
        # chỉ lấy chữ cái và số, chuyển về lowercase
        cleaned = "".join([c.lower() for c in s if c.isalnum()])

        # so sánh 2 đầu bằng vòng lặp
        left, right = 0, len(cleaned) - 1
        while left < right:
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right -= 1
        return True
    
s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))