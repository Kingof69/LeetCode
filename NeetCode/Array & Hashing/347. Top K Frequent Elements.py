from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        # Bước 1: Đếm tần suất
        freq = Counter(nums)  # dict: số -> số lần xuất hiện

        # Bước 2: Sort theo tần suất giảm dần
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        # Bước 3: Lấy k phần tử nhiều nhất
        return [item[0] for item in sorted_items[:k]]