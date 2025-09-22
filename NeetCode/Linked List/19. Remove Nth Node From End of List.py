# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        
        # 1. convert linked list -> list số
        nums = []
        curr = head
        while curr:
            nums.append(curr.val)
            curr = curr.next

        nums.pop(-n)

        # 3. convert lại -> linked list
        dummy = ListNode()
        curr = dummy
        for x in nums:
            curr.next = ListNode(x)
            curr = curr.next
        return dummy.next