class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in "([{":  # ngoặc mở
                stack.append(char)
            else:  # ngoặc đóng
                if not stack:  
                    return False  # đóng nhiều hơn mở
                if stack[-1] != mapping[char]:
                    return False  # loại ngoặc không khớp
                stack.pop()

        # sau khi duyệt xong, nếu stack rỗng thì ok
        return len(stack) == 0
    
# Example usage:
solution = Solution()
print(solution.isValid("()"))          # True
print(solution.isValid("()[]{}"))    # True
print(solution.isValid("(]"))        # False
