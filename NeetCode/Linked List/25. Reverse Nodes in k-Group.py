# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Bước 1: lấy toàn bộ giá trị trong linked list ra array
        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next

        # Bước 2: đảo ngược từng nhóm k trong array
        for i in range(0, len(vals), k):
            if i + k <= len(vals):
                vals[i:i+k] = reversed(vals[i:i+k])

        # Bước 3: xây lại linked list từ array
        dummy = ListNode(0)
        curr = dummy
        for v in vals:
            curr.next = ListNode(v)
            curr = curr.next

        return dummy.next
