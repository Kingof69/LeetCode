from collections import deque

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        q = deque()
        q.append(("", 0, 0))  # (chuỗi hiện tại, số '(' đã dùng, số ')' đã dùng)

        while q:
            cur, open_count, close_count = q.popleft()

            if len(cur) == 2 * n:
                res.append(cur)
                continue

            # Có thể thêm '(' nếu chưa đủ n
            if open_count < n:
                q.append((cur + "(", open_count + 1, close_count))

            # Có thể thêm ')' nếu số ')' chưa vượt quá '('
            if close_count < open_count:
                q.append((cur + ")", open_count, close_count + 1))

        return res

# Example usage:
solution = Solution()   
print(solution.generateParenthesis(3))  # Output: ["((()))","(()())","(())()","()(())","()()()"]