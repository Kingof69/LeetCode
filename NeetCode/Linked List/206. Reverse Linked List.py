# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        # 1. convert linked list -> list số
        nums = []
        curr = head
        while curr:
            nums.append(curr.val)
            curr = curr.next
        
        # 2. đảo list
        nums.reverse()
        
        # 3. convert lại -> linked list
        dummy = ListNode()
        curr = dummy
        for x in nums:
            curr.next = ListNode(x)
            curr = curr.next
        return dummy.next
