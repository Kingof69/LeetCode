from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue

                # Nếu vi phạm (trùng số trong hàng, cột hoặc ô 3x3)
                if val in rows[r] or val in cols[c] or val in boxes[(r // 3) * 3 + c // 3]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[(r // 3) * 3 + c // 3].add(val)

        return True