# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if head == None:
            return head

        curr = None
        temp = None

        while(head):
            temp = head
            head = head.next
            temp.next = curr
            curr = temp
        
        return curr

        
