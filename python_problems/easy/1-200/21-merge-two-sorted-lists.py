# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ptr = ListNode()
        curr = ptr
        while list1 or list2:
            if not list1:
                curr.next = list2
                curr = curr.next
                list2 = list2.next
            elif not list2:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
            elif list1.val <= list2.val:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
            else:
                curr.next = list2
                curr = curr.next
                list2 = list2.next
        return ptr.next
            


        
        
