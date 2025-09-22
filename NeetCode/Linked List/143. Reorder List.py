class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        
        # 1. convert linked list -> list số
        nums = []
        curr = head
        while curr:
            nums.append(curr.val)
            curr = curr.next
        
        # 2. thuật toán reorder
        l, r = 1, len(nums) - 1
        arr = [nums[0]]

        while l < r:
            arr.append(nums[r])
            arr.append(nums[l])
            l += 1
            r -= 1
        if l == r: 
            arr.append(nums[l])
        
        # 3. biến arr thành linked list gốc
        curr = head
        for val in arr:
            curr.val = val 
            if curr.next is None and val != arr[-1]:
                curr.next = ListNode()
            curr = curr.next
        if curr:
            curr = None
