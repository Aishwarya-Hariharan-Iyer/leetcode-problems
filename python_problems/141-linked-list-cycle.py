# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if head == None:
            return False

        while head:
            if head.val == "a":
                return True
            else:
                head.val = "a"
                head = head.next
        
        return False
        
