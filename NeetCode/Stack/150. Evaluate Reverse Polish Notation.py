class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for token in tokens:
            if token not in "+-*/":
                # Nếu là số -> đưa vào stack
                stack.append(int(token))
            else:
                # Nếu là phép toán -> cần ít nhất 2 phần tử
                if len(stack) >= 2:
                    b = stack.pop()   # lấy phần tử trên cùng
                    a = stack.pop()   # lấy phần tử kế tiếp
                    
                    if token == "+":
                        result = a + b
                    elif token == "-":
                        result = a - b
                    elif token == "*":
                        result = a * b
                    elif token == "/":
                        # Chia nguyên làm tròn về 0
                        result = int(a / b)

                    # Đưa kết quả trở lại stack
                    stack.append(result)

        # Sau khi duyệt hết, kết quả cuối cùng nằm trong stack
        return stack[0]
    
# Example usage:
solution = Solution()
print(solution.evalRPN(["2", "1", "+", "3", "*"]))  # Output: 9
print(solution.evalRPN(["4", "13", "5", "/", "+"])) # Output: 6