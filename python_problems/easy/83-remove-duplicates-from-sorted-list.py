# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head
            
        all_nums = dict()
        all_nums[head.val] = 1

        prev = head
        curr = head.next

        while curr:
            if all_nums.get(curr.val, -1) == -1:
                all_nums[curr.val] = 1
                prev = curr
                curr = curr.next
            else:
                prev.next = curr.next
                curr = curr.next
        return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        all_nums = dict()

        prev = head
        recent_val = prev.val
        curr = head.next

        while curr:
            if recent_val != curr.val:
                prev.next = curr
                prev = curr
                recent_val = curr.val
                curr = curr.next
            else:
                curr = curr.next
                prev.next = curr

        return head

        
