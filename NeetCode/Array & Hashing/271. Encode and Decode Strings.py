from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        # Mã hóa: độ dài + '#' + chuỗi
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":   # tìm dấu #
                j += 1
            length = int(s[i:j]) # độ dài chuỗi
            word = s[j+1:j+1+length]
            res.append(word)
            i = j + 1 + length
        return res
