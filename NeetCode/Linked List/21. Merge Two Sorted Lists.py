# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def toList(head: Optional[ListNode]) -> List[int]:
            nums = []
            curr = head
            while curr:
                nums.append(curr.val)
                curr = curr.next
            return nums

        num1 = toList(list1)
        num2 = toList(list2)

        nums = num1 + num2
        nums.sort()

        # convert lại thành linked list
        dummy = ListNode()
        curr = dummy
        for x in nums:
            curr.next = ListNode(x)
            curr = curr.next
        return dummy.next
        dummy = ListNode()
        curr = dummy
        for x in nums:
            curr.next = ListNode(x)
            curr = curr.next
        return dummy.next