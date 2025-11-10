# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        tracker = head
        count = 0

        while tracker != None:
            count += 1
            tracker = tracker.next

        count = count/2 + 1 if count % 2 == 0 else (count + 1)/2

        while count > 1:
            count -= 1
            head = head.next
        
        return head
